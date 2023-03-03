from django.urls import path
from . import views

urlpatterns = [
    path('forum-home/', views.forum-home, name='forum-home'),
    path('forum-register/', views.forum-register, name='forum-register'),
    path('forum-login/', views.forum-login, name='forum-login'),
    path('forum-profile/', views.forum-profile, name='forum-profile'),
    path('forum/', views.forum, name='forum'),
    path('discussion/', views.discussion, name='discussion'),
]