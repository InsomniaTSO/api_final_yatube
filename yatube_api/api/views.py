from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from posts.models import Group, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .viewsets import CustomViewSet


class PostViewSet(CustomViewSet):
    """Представление модели постов"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление модели групп"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class CommentViewSet(CustomViewSet):
    """Представление модели комментариев"""
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    @staticmethod
    def get_post(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("id"))
        return post

    def perform_create(self, serializer):
        post = self.get_post(self)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = self.get_post(self)
        new_queryset = post.comments
        return new_queryset


class FollowViewSet(viewsets.ModelViewSet):
    """Представление модели подписок"""
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        new_queryset = self.request.user.follower.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
