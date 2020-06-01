from django.urls import path
from notification import views

urlpatterns = [
    path('notifications/<str:username>/', views.notifications, "notifications")
]