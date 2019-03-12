#coding=utf-8
from rest_framework import permissions
class LoginOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.session.get('user_id') is not None
        
    def has_object_permission(self, request, view, blog):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        type = request.session.get('type', 1)
        
        if type == 2 or type == 3 :
            return True
        else:
            return False
