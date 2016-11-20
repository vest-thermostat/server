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
    pressure = models.FloatField()

    class Meta:
        ordering = ('created',)

class PublicWeather(Weather):
    def __init__(self):
        super().__init__()

class PrivateWeather(Weather):
    """
    Private weather info for a Vest user.
    """
    owner = models.ForeignKey('users.VestUser', related_name='weather', on_delete=models.CASCADE)

    def __init__(self):
        super().__init__()
