from django.urls import path
from . import views

urlpatterns = [
    # post urls
    path('', views.HomepageView.as_view(), name='home'),
    path('post/', views.board, name='board'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path(
      'posts/<int:post_id>', 
      views.PostDetailView.as_view(), 
      name='post-detail'
    ),
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

    # timetable urls
    path('timetable/', views.timetable, name='timetable'),
    # path('course/<int:course_id>/', views.course_detail, name='course-detail'),
    path(
      'timetable/<int:course_id>/delete/', 
      views.delete_course, 
      name='course-delete'),

    # settings urls
    path('settings/', views.settings, name='settings'),

    # board uls
    path('board/', views.BoardView.as_view(), name='board'),
]
