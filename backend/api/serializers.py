from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Post, Comment, Like, CommentLike


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField()
    author = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    comment_likes = serializers.ReadOnlyField()

    def create(self, validated_data):
        comment_list = Comment(**validated_data)
        comment_list.save()
        return comment_list

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.text = validated_data.get('text', instance.text)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.comment_likes = validated_data.get('comment_likes', instance.comment_likes)
        instance.save()
        return instance


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    author = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    post_likes = serializers.ReadOnlyField()
    post_comments = serializers.ReadOnlyField()
    comments = CommentSerializer(read_only=True, many=True)

    def create(self, validated_data):
        post_list = Post(**validated_data)
        post_list.save()
        return post_list

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.post_likes = validated_data.get('post_likes', instance.post_likes)
        instance.post_comments = validated_data.get('post_comments', instance.post_comments)
        instance.save()
        return instance



class LikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'

class CommentLikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = UserSerializer(read_only=True)
    comment = CommentSerializer(read_only=True)

    class Meta:
        model = CommentLike
        fields = '__all__'

