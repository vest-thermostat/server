from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners to see it
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
        # if request.method in permissions.SAFE_METHODS:
        #     # Read permissions are allowed for owner.
        #     return obj.owner == request.user
        # else:
        #     # No Write permissions
        #     return False
