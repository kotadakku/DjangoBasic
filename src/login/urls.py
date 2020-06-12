from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('index/', views.loginClass.as_view(), name ='index'),
    path('result/', views.result, name ='result'),
    path('post/', views.PostClass.as_view(), name='post'),
    path('resultde/', views.result_decorators, name ='resultde'),
]