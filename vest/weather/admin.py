from django.contrib import admin
from .models import PrivateWeather, PersonalTemperature

@admin.register(PrivateWeather)
class PrivateWeatherAdmin(admin.ModelAdmin):
    list_display = ['created', 'temperature', 'humidity', 'owner']

@admin.register(PersonalTemperature)
class PersonalTemperatureAdmin(admin.ModelAdmin):
    list_display = ['created', 'temperature', 'owner']
