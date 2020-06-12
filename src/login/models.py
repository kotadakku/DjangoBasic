from django.db import models

# Create your models here.
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    choice = ((0, "Girl"), (1, "Boy"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=choice, default=0)



class Post(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=2000)
    time_pub = models.DateTimeField(default=now())
    def __str__(self):
        return self.title
