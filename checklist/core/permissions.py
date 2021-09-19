from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # print('aaaaaa..   ... {} ... {}'.format(obj, dir(obj)))
        # print('object user: {} \t requested user... {}\n\n'.format(obj.user, request.user))
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user
