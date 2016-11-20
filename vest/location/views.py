from rest_framework import generics
from rest_framework import permissions

from location.models import UserLocation
from location.serializers import LocationSerializer
from location.permissions import IsOwner

class LocationList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = UserLocation.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (
            permissions.IsAuthenticated,
            IsOwner,
    )

class LocationDetail(generics.RetrieveAPIView):
    queryset = UserLocation.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (
            permissions.IsAuthenticated,
            IsOwner,
    )
