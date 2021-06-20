from rest_framework import viewsets, status
from rest_framework.decorators import action
from posts.serializers import (
    PostSerializer,
    CommentSerializer
)

from posts.models import (
    Post, Comment
)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import F


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset to handle requests related to Post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=["post"], detail=True, url_path="upvote")
    def upvote(self, request, pk):
        get_object_or_404(self.queryset, pk=pk)
        self.queryset.filter(pk=pk).update(upvotes=F("upvotes") + 1)
        serializer = self.get_serializer(self.queryset.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)


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
