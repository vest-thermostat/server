from django.db import models


class PersonalTemperature(models.Model):
    """
    Temperature set by the user.
    """
    created = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    owner = models.ForeignKey('users.VestUser', on_delete=models.CASCADE)

    class Meta:
        get_latest_by = "created"
        ordering = ('-created',)


class Weather(models.Model):
    """
    A model for the weather datas.
    """
    created = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    class Meta:
        ordering = ('-created',)


class PrivateWeather(models.Model):
    """
    Private weather info for a Vest user.
    """
    created = models.DateTimeField(auto_now_add=True)
    # fromThermostat = models.CharField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    # heat = models.BooleanField(default=False)
    owner = models.ForeignKey('users.VestUser', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

from weather import signals
