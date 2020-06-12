from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View

from .forms import PostForm, SendEmail


def index(request):
    a = PostForm(request.POST or None)
    if a.is_valid():
        a.save()
        a = PostForm()
    return render(request, 'forms/postforms.html', {'a':a})

def savePost(request):
    if request.method == 'POST':
        a = PostForm(request.POST)
        if a.is_valid():
            title = a.cleaned_data['title']
            content = a.cleaned_data['content']
            a.save()
            data = {'t': title, 'c':content}
            return render(request,'forms/results_post.html', data)
        else:
            return HttpResponse('is_valid')
    else:
        return HttpResponse('not post')
class sendEmail(View):
    def get(self, request):
        e = SendEmail()
        return render(request, 'forms/sendemail.html', {'e':e})
    def post(self, request):
        a = SendEmail(request.POST)
        if (a.is_valid()):
            name = a.cleaned_data['name']
            email = a.cleaned_data['email']
            content = a.cleaned_data['content']
            cc = a.cleaned_data['cc']
            g = {'n': name, 'e': email, 'c': content, 'cc': cc}
            return render(request, 'forms/results_email.html', g)
        else:
            return HttpResponse('no valid')
