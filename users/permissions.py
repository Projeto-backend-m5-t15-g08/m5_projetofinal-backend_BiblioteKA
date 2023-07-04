from rest_framework import permissions


class IsColaborator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_superuser
        return True