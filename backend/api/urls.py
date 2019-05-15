from django.urls import path

from api import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='home'),
    #path('posts/<int:pk>/', views.PostDetailList.as_view()),
    path('posts/<int:pk>/', views.PostCrud.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('posts/<int:pk>/comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentCrud.as_view()),
    path('posts/<int:pk>/likes/', views.LikeList.as_view()),
    path('like_post/<int:pk>/', views.LikeDelete.as_view()),
    path('like_comment/<int:pk>/', views.CommentLikeDelete.as_view()),
    path('comments/<int:pk>/likes/', views.CommentLikeList.as_view()),

]