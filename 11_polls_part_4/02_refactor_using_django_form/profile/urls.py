from django.urls import path
from . import views


app_name = 'profile'

urlpatterns = [
    path('signout/', views.signout, name='signout'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/following', views.following, name='following'),
    path('<str:username>/followers', views.followers, name='followers'),
    path('<str:username>/follow', views.follow, name='follow'),
    path('<str:username>/stopfollow', views.stopfollow, name='stopfollow'),
    
]