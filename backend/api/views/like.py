from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import CommentLike, Like
from api.serializers import LikeSerializer, CommentLikeSerializer


class Like(generics.RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Like.objects.all()


class CommentLike(generics.RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = CommentLikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = CommentLike.objects.all()