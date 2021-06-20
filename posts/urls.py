from rest_framework import routers
from posts import views

router = routers.DefaultRouter()
router.register("posts", views.PostViewSet, basename="posts")
router.register("comments", views.CommentViewSet, basename="comments")

urlpatterns = router.urls
