from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, req, view):
        if req.method == 'POST':
            return True

        return False
