from django.urls import path

from . import views
app_name='polls'
urlpatterns = [
    path('index', views.index, name ='index'),
    path('detail/<int:question_id>', views.detail, name ='detail'),
    path('result/<int:question_id>', views.result, name ='result'),
    path('vote/<int:question_id>', views.vote, name ='vote')

]
