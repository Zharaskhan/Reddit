from django.contrib import admin

from api.models import Post, Comment, Like, CommentLike

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(CommentLike)

