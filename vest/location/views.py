from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import TemplateHTMLRenderer

from location.models import UserLocation, UserJourney
from location.serializers import LocationSerializer, JourneySerializer
from users.permissions import IsOwner

class LocationList(viewsets.ModelViewSet):
    queryset = UserLocation.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (
            permissions.IsAuthenticated,
            IsOwner,
    )
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'location.html'

    def get_queryset(self):
        return UserLocation.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        if not serializer.is_valid():
            raise ValidationError()

        serializer.save(owner=self.request.user)

class JourneyList(viewsets.ModelViewSet):
    queryset = UserJourney.objects.all()
    serializer_class = JourneySerializer

    def get_queryset(self):
        return UserJourney.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        raise ValidationError()
