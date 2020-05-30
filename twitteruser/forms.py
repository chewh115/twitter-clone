from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import TwitterUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = TwitterUser
        fields = ('display_name', 'age')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = TwitterUser
        fields = ('display_name', 'age')


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=50)
    age = forms.IntegerField()