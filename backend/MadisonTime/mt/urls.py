from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.board, name='board'),
    path('timetable/', views.timetable, name='timetable'),
]
