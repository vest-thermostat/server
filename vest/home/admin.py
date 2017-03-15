from django.contrib.gis import admin
from .models import HeatTypeDefinition, HomeDaySchedule, HeatRange, ThermostatState

@admin.register(HeatTypeDefinition)
class HeatTypeDefinitionAdmin(admin.ModelAdmin):
    list_display = ['owner', 'type', 'temperature']

@admin.register(HomeDaySchedule)
class HomeDayScheduleAdmin(admin.ModelAdmin):
    list_display = ['owner', 'day']

@admin.register(HeatRange)
class HeatRangeAdmin(admin.ModelAdmin):
    list_display = ['day', 'type', 'start', 'finish']

@admin.register(ThermostatState)
class StateAdmin(admin.ModelAdmin):
    list_display = ['created', 'state', 'owner']
