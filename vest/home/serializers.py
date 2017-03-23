from rest_framework import serializers
from .models import HeatTypeDefinition, HomeDaySchedule, HeatRange, ThermostatState

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThermostatState
        fields = (
            'created',
            'state',
        )

class HeatRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatRange
        fields = (
            'type',
            'start',
            'finish',
        )

class HomeDayScheduleSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField() # HeatRangeSerializer()

    def get_data(self, obj):
        result = []
        for hr in HeatRange.objects.all().filter(day=obj.id):
            result.append(HeatRangeSerializer(hr).data)

        return result

    class Meta:
        model = HomeDaySchedule
        fields = (
            'id',
            'owner',
            'day',
            'data',
        )
