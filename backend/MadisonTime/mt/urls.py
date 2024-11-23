from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('post/', views.board, name='board'),
    path('timetable/', views.timetable, name='timetable'),
    path(
      'posts/<int:post_id>', 
      views.PostDetailView.as_view(), 
      name='post-detail'
    ),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path(
      'posts/<int:post_id>/edit',
      views.PostUpdateView.as_view(),
      name='post-update'),
    path(
      'posts/<int:post_id>/delete',
      views.delete_post,
      # views.PostDeleteView.as_view(),
      name='post-delete'),
    path(
      'comment/<int:comment_id>/delete/', 
      views.delete_comment, 
      name='comment-delete'),
]
