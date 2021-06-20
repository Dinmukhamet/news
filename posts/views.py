from rest_framework import viewsets
from posts.serializers import (
    PostSerializer,
    CommentSerializer
)

from posts.models import (
    Post, Comment
)


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset to handle requests related to Post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset to handle requests related to Comment
    Two filter options allowed:
    1) Get by specific post
    2) Get by parent comment
    """
    filterset_fields = ['post', 'parent']
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
