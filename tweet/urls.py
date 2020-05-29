from django.urls import path
from tweet import views

urlspatterns =[
    path('', views.tweetindex, "tweethome")
]