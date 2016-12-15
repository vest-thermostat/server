from django.db import models

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
        ordering = ('created',)

class PrivateWeather(models.Model):
    """
    Private weather info for a Vest user.
    """
    created = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    owner = models.ForeignKey('users.VestUser', related_name='weather', on_delete=models.CASCADE)
