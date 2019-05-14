from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from api.models import Comment, Post
from api.serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class CommentList(generics.ListCreateAPIView):
	authentication_classes = (TokenAuthentication,)
	serializer_class = CommentSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, )

	def get_queryset(self):
		post = Post.objects.get(pk=self.kwargs.get('pk'))
		queryset= Comment.objects.filter(origin_post=post)
		return queryset

	def perform_create(self, serializer):
		post = Post.objects.get(pk=self.kwargs.get('pk'))
		return serializer.save(author=self.request.user, origin_post=post)



class CommentCrud(APIView):
    def get_object(self,pk):
        try:
            return Comment.objects.filter(author=self.request.user).get(id=pk)
        except Comment.DoesNotExist:
            return Response({'error: not found'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
            comment=self.get_object(pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)

    def put(self,request,pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

