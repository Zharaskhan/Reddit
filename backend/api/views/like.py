from django.http import Http404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import Post, Comment
from api.serializers import LikeSerializer


class Like(generics.RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        try:
            category = Post.objects.get(id=self.kwargs['pk'])
        except Post.DoesNotExist:
            raise Http404

        queryset = category
        return queryset


class CommentLike(generics.RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        # category = get_object_or_404(Category, id=self.kwargs['pk'])
        try:
            comment = Comment.objects.get(id=self.kwargs['pk'])
        except Comment.DoesNotExist:
            raise Http404

        queryset = comment
        return queryset
