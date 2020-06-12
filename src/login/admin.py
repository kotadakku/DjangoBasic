from django.contrib import admin

# Register your models here.
from .models import Post, MyUser

admin.site.register(Post)
admin.site.register(MyUser)
