from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'v1/posts', PostViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/posts/(?P<id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register(r'v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
