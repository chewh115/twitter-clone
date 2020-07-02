from django.urls import path
from . import views

urlpatterns =[
    path('createtweet/', views.CreateTweetView.as_view(), name="createtweet"),
    path('tweet/<int:pk>', views.TweetDetail.as_view(), name="tweetdetail")
]