from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners to see it
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsSelf(permissions.BasePermission):
    """
    """
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username
