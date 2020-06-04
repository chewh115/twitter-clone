from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('<str:username>/', views.userdetail, name='userdetail'),
    path('<str:username>/follow/', views.follow, name='follow'),
    path('<str:username>/unfollow/', views.unfollow, name='unfollow')
]