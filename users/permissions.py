from rest_framework import permissions


class UserIsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderators').exists()


class UserIsNotModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.groups.filter(name='Moderators').exists()


class IsCreator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.creator == request.user:
            return True
        return False
