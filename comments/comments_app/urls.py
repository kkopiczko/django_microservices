from django.urls import path, include
from .views import CommentAPIView, PostCommentAPIView

urlpatterns = [
    path('posts/<str:pk>/comments', PostCommentAPIView.as_view()),
    path('comments', CommentAPIView.as_view())
]