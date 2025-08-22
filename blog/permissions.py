from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Read-only for anyone; write allowed only to the object's author or staff.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, 'author', None) == request.user or request.user.is_staff
