from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from .models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser


# Create your views here.
def notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(notified_user=request.user, viewed=False)
        notifs = []
        for notification in notifications:
            notifs.append(notification)
            notification.viewed = True
            notification.save()
        user = TwitterUser.objects.get(username=request.user.username)
        return render(request, 'notifications.html', {'notifications': notifs})
    return redirect('/login/')