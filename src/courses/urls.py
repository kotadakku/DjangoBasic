from django.urls import path

from . import views
app_name = 'courses'
urlpatterns = [

    path('<int:id>/', views.CoursesView.as_view(), name="detail"),
    path('', views.CoursesListView.as_view(), name="list"),
    path('testapi/', views.GetAllCource.as_view(), name="testapi"),
]