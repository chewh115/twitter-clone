from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from .models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser


# Create your views here.
def notifs(request):
    notifications = Notification.objects.filter(notified_user=request.user, viewed=False)
    if notifications:
        for notification in notifications:
            notification.viewed = True
            notification.save()
        user = TwitterUser.objects.get(username=request.user.username)
        return render(
            request,
            'notifications.html',
            {'notifications': notifications, 'user': user})
    return render(request, 'notifications.html')