from rest_framework.permissions import BasePermission
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)