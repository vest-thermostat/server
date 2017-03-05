from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import time


HEAT_TYPE = (
    ('Standard', 'Standard'),
    ('Hot', 'Hot'),
    ('Eco', 'Eco'),
    ('Night', 'Night'),
)


DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


class HeatRange(models.Model):
    day = models.ForeignKey('home.HomeDaySchedule', on_delete=models.CASCADE)
    type = models.CharField(blank=False, choices=HEAT_TYPE, max_length=10)
    start = models.TimeField(blank=False)
    finish = models.TimeField(blank=False)

    def get_overlappings(self, start, finish):
        sameDayHeatRange = HeatRange.objects.filter(day=self.day)

        overlappingHeatRangeStart = sameDayHeatRange.filter(start__gte=self.start, start__lte=self.finish)
        overlappingHeatRangeEnd = sameDayHeatRange.filter(finish__gte=self.start, finish__lte=self.finish)

        return set(overlappingHeatRangeStart) | set(overlappingHeatRangeEnd)

    def save(self, *args, **kwargs):
        for x in self.get_overlappings(self.start, self.finish):
            x.delete()

        super(HeatRange, self).save(*args, **kwargs)


class HomeDaySchedule(models.Model):
    owner = models.ForeignKey('users.VestUser', on_delete=models.CASCADE)
    day = models.CharField(blank=False, choices=DAYS_OF_WEEK, max_length=10)

    def save(self, *args, **kwargs):
        # Checking there is no overlapping day.
        sameOwnerDaySchedule = HomeDaySchedule.objects.filter(owner=self.owner, day=self.day)

        if sameOwnerDaySchedule:
            return

        instance = super(HomeDaySchedule, self).save(*args, **kwargs)


@receiver(post_save, sender=HomeDaySchedule)
def populate_heat_range(sender, instance, **kwargs):
    # Generate defaults timerange
    for day in DAYS_OF_WEEK:
        HeatRange(day=instance, type="Night", start=time(hour=0), finish=time(hour=7)).save()
        HeatRange(day=instance, type="Standard", start=time(hour=7), finish=time(hour=23)).save()
        HeatRange(day=instance, type="Eco", start=time(hour=23), finish=time(hour=0)).save()


class HeatTypeDefinition(models.Model):
    owner = models.ForeignKey('users.VestUser', on_delete=models.CASCADE)
    type = models.CharField(blank=False, choices=HEAT_TYPE, max_length=10)
    temperature = models.FloatField()

    def save(self, *args, **kwargs):
        sameOwnerHeatType = HeatTypeDefinition.objects.filter(owner=self.owner, type=self.type)

        if sameOwnerHeatType:
            return

        super(HeatTypeDefinition, self).save(*args, **kwargs)
