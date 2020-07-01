from django.urls import path
from . import views

urlpatterns =[
    path('createtweet/', views.CreateTweetView.as_view(), name="createtweet"),
    path('tweet/<int:id>', views.tweetdetail, name="tweetdetail")
]