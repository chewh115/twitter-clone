from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.index, name='userhome')
]