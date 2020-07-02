from django.shortcuts import render, reverse, HttpResponseRedirect, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .forms import TweetForm
from .models import Tweet
from datetime import datetime
from notification.models import Notification
from twitteruser.models import TwitterUser
import re

# Create your views here.

class CreateTweetView(View):
    form = TweetForm
    initial = {'key': 'value'}
    template_name='createtweet.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {'form': self.form})
        else:
            return redirect('/login/')

    def post(self, request):
        form = self.form(request.POST)
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
        return render(request, self.template_name, {'form': form})

def tweetdetail(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweetdetail.html', {'tweet': tweet})

class TweetDetail(DetailView):
    template_name = 'tweetdetail.html'
    model = Tweet

    def get_queryset(self):
        self.tweet = get_object_or_404(Tweet, id=self.kwargs['pk'])
        return super().get_queryset()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tweet'] = self.tweet
        return context
    


