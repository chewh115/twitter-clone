from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm
from .models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {}
        context['user_info'] = request.user
        context['tweets'] = Tweet.objects.filter(author__in=request.user.following.all()).order_by(
            '-time_tweeted')
        context['notifications'] = Notification.objects.filter(notified_user=request.user, viewed=False)
        return render(request, 'index.html', context)
    return redirect('/login/')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            TwitterUser.objects.create(
                username = user_info['username'],
                display_name = user_info['display_name'],
                age = user_info['age']
            )
            user = TwitterUser.objects.last()
            user.set_password(user_info['password'])
            user.following.add(user)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def sidebar():
    pass

def userdetail(request, username):
    user_info = {}
    user = TwitterUser.objects.get(username=username)
    user_info['user'] = user
    user_info['tweets'] = Tweet.objects.filter(author_id=user.id).order_by('-time_tweeted')
    if request.user.is_authenticated:
        user_info['notifications'] = Notification.objects.filter(notified_user=request.user, viewed=False)
    return render(request, 'userdetail.html', user_info)


def follow(request, username):
    active_user = TwitterUser.objects.get(username=request.user.username)
    follow_user = TwitterUser.objects.get(username=username)
    active_user.following.add(follow_user.id)
    active_user.save()
    return HttpResponseRedirect(reverse('userdetail', args=(username,)))


def unfollow(request, username):
    active_user = TwitterUser.objects.get(username=request.user.username)
    unfollow_user = TwitterUser.objects.get(username=username)
    active_user.following.remove(unfollow_user.id)
    active_user.save()
    return HttpResponseRedirect(reverse('userdetail', args=(username,)))