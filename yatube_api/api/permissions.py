from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешение на редактирование только автором"""
    message = 'Изменение и удаление чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class ReadOnly(permissions.BasePermission):
    """Разрешение на чтение любым пользователем"""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
