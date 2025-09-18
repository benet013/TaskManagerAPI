from rest_framework import permissions

    
class PostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'
    
    