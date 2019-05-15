from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from api.models import Post
from rest_framework.response import Response
from api.serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response

class PostList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    model = Post
    template_name = 'home.html'

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class PostCrud(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.filter(author=self.request.user).get(id=pk)
        except Post.DoesNotExist:
            return Response({'error: not found'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
            #task_list=self.get_object(pk)
            task_list = Post.objects.get(id=pk)
            serializer = PostSerializer(task_list)
            return Response(serializer.data)

    def put(self,request,pk):
        task_list = self.get_object(pk)
        serializer = PostSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task_lists = self.get_object(pk)
        task_lists.delete()



