from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedViewSet

# Initialize the router
router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed', UserFeedViewSet, basename='user-feed')

urlpatterns = router.urls
