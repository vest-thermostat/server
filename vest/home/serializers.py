from rest_framework import serializers
from .models import HeatTypeDefinition, HomeDaySchedule, HeatRange

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
        return HeatRangeSerializer(HeatRange.objects.all().filter(day=obj.id)).data

    class Meta:
        model = HomeDaySchedule
        fields = (
            'id',
            'owner',
            'day',
            'data',
        )
