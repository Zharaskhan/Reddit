from django.contrib.auth.models import User
from django.db import models


class PostManager(models.Manager):
    def for_user(self, user):
        return self.filter(author=user)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title',max_length=100)
    body = models.TextField('Body', max_length=600)
    created_at = models.DateTimeField('Created', auto_now_add=True, null=False)

    objects = PostManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return '{}: {} at {}'.format(self.author, self.title, self.created_at)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Text', max_length=600)
    created_at = models.DateTimeField('Created', auto_now_add=True, null=False)
    origin_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'From {} to the  {} at {}'.format(self.author, self.origin_post.title, self.created_at)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                    related_name='likes')

    def __str__(self):
        return '{} liked {}'.format(self.author, self.post.title)

    class Meta:
        unique_together = ('author', 'post')


class CommentLike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                    related_name='likes')

    def __str__(self):
        return '{} liked comment: {}'.format(self.author, self.comment.id)

    class Meta:
        unique_together = ('author', 'comment')