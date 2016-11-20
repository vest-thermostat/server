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
