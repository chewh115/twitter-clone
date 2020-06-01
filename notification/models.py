from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your models here.
class Notification(models.Model):
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        related_name='notif_tweet'
        )
    notified_user = models.ForeignKey(TwitterUser,
        on_delete=models.CASCADE,
        related_name='notified_user'
        )
    viewed = models.BooleanField(default=False)