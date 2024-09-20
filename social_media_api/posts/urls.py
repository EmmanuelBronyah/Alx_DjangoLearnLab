from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeed
from django.urls import path, include

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

custom_urls = [
    path('feed/', UserFeed.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
]

urlpatterns = [
    path('', include(router.urls)),
] + custom_urls
