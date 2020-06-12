from django.db import models

# Create your models here.
from django.utils.timezone import now


class Post(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField(max_length=1000)
    time_create = models.DateTimeField(default=now())
    

