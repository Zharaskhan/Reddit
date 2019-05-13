from django.urls import path

from api import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetailList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetailList.as_view()),
    path('like_post/<int:pk>/', views.PostList.as_view()),
    path('like_comment/<int:pk>/', views.CommentLike.as_view()),
]