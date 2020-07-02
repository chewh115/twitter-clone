from django.shortcuts import render, reverse, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.views.generic import DetailView
from .forms import SignupForm
from .models import TwitterUser
from tweet.models import Tweet

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {}
        context['user_info'] = request.user
        context['tweets'] = Tweet.objects.filter(author__in=request.user.following.all()).order_by(
            '-time_tweeted')
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


class SignupFormView(View):
    form = SignupForm
    initial = {'key': 'value'}
    template_name='signup.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    
    def post(self, request):
        form = self.form(request.POST)
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
        return render(request, self.template_name, {'form': form})


class UserDetail(DetailView):
    model = TwitterUser
    template_name = 'userdetail.html'

    def get_queryset(self):
        self.user = get_object_or_404(TwitterUser, id=self.kwargs['pk'])
        return super().get_queryset()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['tweets'] = Tweet.objects.filter(author_id=self.user.id).order_by('-time_tweeted')
        return context
    


def follow(request, pk):
    if request.user.is_authenticated:
        active_user = TwitterUser.objects.get(pk=request.user.pk)
        follow_user = TwitterUser.objects.get(pk=pk)
        active_user.following.add(follow_user.id)
        active_user.save()
        return HttpResponseRedirect(reverse('userdetail', args=(pk,)))
    return redirect('/login/')


def unfollow(request, pk):
    if request.user.is_authenticated:
        active_user = TwitterUser.objects.get(pk=request.user.pk)
        unfollow_user = TwitterUser.objects.get(pk=pk)
        active_user.following.remove(unfollow_user.id)
        active_user.save()
        return HttpResponseRedirect(reverse('userdetail', args=(pk,)))
    return redirect('/login/')