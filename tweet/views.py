from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import TweetForm
from .models import Tweet
from datetime import datetime

# Create your views here.
def createtweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            new_tweet = form.cleaned_data
            Tweet.objects.create(
                tweet = new_tweet['tweet'],
                time_tweeted = datetime.now(),
                author = request.user
            )
            return HttpResponseRedirect(reverse('home'))
    form = TweetForm()
    return render(request, 'createtweet.html', {'form': form})