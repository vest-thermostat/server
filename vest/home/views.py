from rest_framework import viewsets, permissions
from .models import HomeDaySchedule
from .serializers import HomeDayScheduleSerializer

class HomeView(viewsets.ModelViewSet):
    """
    """
    queryset = HomeDaySchedule.objects.all()
    serializer_class = HomeDayScheduleSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        return HomeDaySchedule.objects.filter(owner=self.request.user)
