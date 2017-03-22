from rest_framework import viewsets, permissions
from rest_framework.renderers import TemplateHTMLRenderer
from .models import HomeDaySchedule, ThermostatState
from .serializers import HomeDayScheduleSerializer, StateSerializer

class StateView(viewsets.ModelViewSet):
    """
    """
    queryset = ThermostatState.objects.all()
    serializer_class = StateSerializer

    def get_queryset(self):
        return ThermostatState.objects.filter(owner=self.request.user)

class HomeView(viewsets.ModelViewSet):
    """
    """
    queryset = HomeDaySchedule.objects.all()
    serializer_class = HomeDayScheduleSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'preference.html'

    def get_queryset(self):
        return HomeDaySchedule.objects.filter(owner=self.request.user)
