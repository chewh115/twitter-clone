from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('twitteruser/<int:pk>/', views.UserDetail.as_view(), name='userdetail'),
    path('twitteruser/<int:pk>/follow/', views.follow, name='follow'),
    path('twitteruser/<int:pk>/unfollow/', views.unfollow, name='unfollow')
]