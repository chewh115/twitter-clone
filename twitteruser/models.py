from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    REQUIRED_FIELDS = ['display_name', 'age']