from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from .forms import TweetForm
from .models import Tweet
from datetime import datetime
from notification.models import Notification
from twitteruser.models import TwitterUser
import re

# Create your views here.
def createtweet(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = TweetForm(request.POST)
            if form.is_valid():
                tweet_data = form.cleaned_data
                new_tweet = Tweet.objects.create(
                    tweet = tweet_data['tweet'],
                    time_tweeted = datetime.now(),
                    author = request.user
                )
                new_tweet.save()
                to_notify = re.findall(r"\@(\w*)\b", tweet_data['tweet'])
                for user in to_notify:
                    new_notif = Notification.objects.create(
                        tweet = new_tweet,
                        notified_user = TwitterUser.objects.get(username=user),
                        viewed=False
                    )
                    new_notif.save()
                return HttpResponseRedirect(reverse('home'))
        form = TweetForm()
        return render(request, 'createtweet.html', {'form': form})
    return redirect('/login/')


def tweetdetail(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweetdetail.html', {'tweet': tweet})