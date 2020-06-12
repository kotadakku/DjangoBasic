from django.urls import path, include

from . import views
app_name ='forms'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('send/', views.sendEmail.as_view(), name ='send'),
    path('save/', views.savePost, name ='save')
]