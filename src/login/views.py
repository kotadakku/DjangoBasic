from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views import View

from .forms import PostForm


class loginClass(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is None:
            return HttpResponse("User is valid")
        else:
            login(request, user)
            a = PostForm()
            return render(request, 'login/post.html', {'a':a})

class PostClass(LoginRequiredMixin, View):
    login_url = '../index'
    def get(self, request):
        a =PostForm()
        return render(request,'login/post.html', {'a':a})
    def post(self, request):
        a = PostForm(request.POST)
        if a.is_valid():
            if request.user.has_perm('login.add_post'):
                a.save()
                return HttpResponse('Success!')
            else:
                return HttpResponse('You do not permission')
        else:
            return HttpResponse('Is valid')



def  result(request):
    if not request.user.is_authenticated:
        return HttpResponse('Please, log in!')
    else:
        return HttpResponse('Ok! You are already logged in!')


@decorators.login_required(login_url='../index')
def  result_decorators(request):
    return HttpResponse('Ok! You are already logged in!')





