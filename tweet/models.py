from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    time_tweeted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='tweet_author'
        )
    
    def __str__(self):
        return self.tweet