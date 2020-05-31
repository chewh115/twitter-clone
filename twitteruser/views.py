from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm
from .models import TwitterUser
from tweet.models import Tweet

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {}
        context['user_info'] = request.user
        tweets = Tweet.objects.filter
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
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def userdetail(request, id):
    user = TwitterUser.objects.get(id=id)
    return render(request, 'userdetail.html', {'user': user})