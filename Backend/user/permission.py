#coding=utf-8
from rest_framework import permissions
from .models import User
class LoginOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.session.get('user_id') is not None
        
    # def has_object_permission(self, request, view, blog):
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     return blog.owner.id == request.session.get('user_id')

class UserOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.session.get('type', 1) == 3 :
            return True

        if request.method=="POST":
            rating = request.data.get('rating',-1)
            acc = request.data.get('ac',-1)
            sub = request.data.get('submit',-1)
            sco = request.data.get('score',-1)
            type = request.data.get('type',-1)
            if type != -1:
                return False
            if rating != "" or acc !="" or sub !="" or sco!="":
                if rating == -1:
                    return True
                return False
            else:
                return True
        
        data = request.data
        username = data.get('username')
        rating = data.get('rating',-1)
        score = data.get('score',-1)
        ac = data.get('ac',-1)
        submit = data.get('submit',-1)
        
        if rating != -1 or score != -1 or ac != -1 or submit != -1:
            return False

        userid = request.session.get('user_id', None)
        if userid == username or request.session.get('type', 1) == 3 :
            return True
        else:
            return False 

    # def has_object_permission(self, request, view, blog):
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     return False
    #     # data = request.data
    #     # print(data.get('rating'))
    #     # print(data.get('des'))
    #     # return data.get('rating',-1) == -1

            
class UserPUTOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != "PUT":
            return False
        
        data = request.data
        username = data.get('username')
        userid = request.session.get('user_id', None)
        if userid == username or request.session.get('type', 1) == 3 :
            return True
        else:
            return False 
    
    def has_object_permission(self, request, view, blog):
        if request.method != "PUT":
            return False
        data = request.data
        username = data.get('username')
        userid = request.session.get('user_id', None)
        if userid == username or request.session.get('type', 1) == 3 :
            return True
        else:
            return False 
            

class AuthPUTOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != "PUT":
            return False
        if request.session.get('type', 1) == 3 :
            return True
        else:
            return False 
    
    def has_object_permission(self, request, view, blog):
        if request.method != "PUT":
            return False
        if request.session.get('type', 1) == 3 :
            return True
        else:
            return False 