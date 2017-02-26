from django.db import models
from datetime import time


HEAT_TYPE = (
    (0, 'Standard'),
    (1, 'Hot'),
    (2, 'Eco'),
    (3, 'Night'),
)


DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class HeatRange(models.Model):
    day = models.ForeignKey('home.HomeDaySchedule', on_delete=models.CASCADE)
    type = models.CharField(blank=False, choices=HEAT_TYPE, max_length=10)
    start = models.TimeField(blank=False)
    finish = models.TimeField(blank=False)

    def get_overlappings(start, finish):
        sameDayHeatRange = HeatRange.objects.filter(day=self.day)

        overlappingHeatRangeStart = sameDayHeatRange.filter(start__gte=self.start, start__lte=self.finish)
        overlappingHeatRangeEnd = sameDayHeatRange.filter(finish__gte=self.start, finish__lte=self.finish)

        return set(overlappingHeatRangeStart) | set(overlappingHeatRangeEnd)

    def save(self, *args, **kwargs):
        for x in self.get_overlapping(self.start, self.finish):
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

        instance = super(HomeDaySchedule, self).save(i*args, **kwargs)

        # Generate defaults timerange
        for day in DAYS_OF_WEEK:
            HeatRange.save(day=instance, type="Night", start=time(hour=0), finish=time(hour=7))
            HeatRange.save(day=instance, type="Standard", start=time(hour=7), finish=time(hour=23))
            HeatRange.save(day=instance, type="Eco", start=time(hour=23), finish=time(hour=0))


class HeatTypeDefinition(models.Model):
    owner = models.ForeignKey('users.VestUser', on_delete=models.CASCADE)
    type = models.CharField(blank=False, choices=HEAT_TYPE, max_length=10)
    temperature = models.FloatField()

    def save(self, *args, **kwargs):
        sameOwnerHeatType = HeatTypeDefinition.objects.filter(owner=self.owner, type=self.type)

        if sameOwnerHeatType:
            return
        else:
            super(HeatTypeDefinition, self).save(i*args, **kwargs)
