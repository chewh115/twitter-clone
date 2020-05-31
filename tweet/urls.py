from django.urls import path
from . import views

urlpatterns =[
    path('createtweet/', views.createtweet, name="createtweet"),
    path('tweet/<int:id>', views.tweetdetail, name="tweetdetail")
]