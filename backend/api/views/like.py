from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from api.models import CommentLike, Like, Post, Comment
from api.serializers import LikeSerializer, CommentLikeSerializer
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

class LikeList(generics.ListCreateAPIView):
	authentication_classes = (TokenAuthentication,)
	serializer_class = LikeSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, )
	#queryset = Like.objects.all()

	def get_queryset(self):
		post = Post.objects.get(pk=self.kwargs.get('pk'))
		queryset= post.likes
		return queryset


	def perform_create(self, serializer):
		post = Post.objects.get(pk=self.kwargs.get('pk'))
		return serializer.save(author=self.request.user, post=post)


class LikeDelete(APIView):
	def get_object(self,pk):
		try:
			return Like.objects.filter(author=self.request.user).get(id=pk)
		except ObjectDoesNotExist:
			return Response({'error: not found'},status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, pk):
		like = self.get_object(pk)
		like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class CommentLikeList(generics.ListCreateAPIView):
	authentication_classes = (TokenAuthentication,)
	serializer_class = CommentLikeSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, )
	#queryset = CommentLike.objects.all()
	def get_queryset(self):
		comment = Comment.objects.get(pk=self.kwargs.get('pk'))
		queryset= comment.likes
		return queryset

	def perform_create(self, serializer):
		comment = Comment.objects.get(pk=self.kwargs.get('pk'))
		return serializer.save(author=self.request.user, comment=comment)



class CommentLikeDelete(APIView):
	def get_object(self,pk):
		try:
			return CommentLike.objects.filter(author=self.request.user).get(id=pk)
		except ObjectDoesNotExist:
			return Response({'error: not found'},status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, pk):
		comment_like = self.get_object(pk)
		comment_like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

