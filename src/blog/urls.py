from django.urls import path

from . import views
app_name ='blog'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name="list"),
    path('<int:id>/', views.ArticleDetailView.as_view(), name="detail"),
    path('create/', views.ArticleCreateView.as_view(), name="create"),
    path('<int:id>/update/', views.ArticleUpdateView.as_view(), name="update"),
    path('<int:id>/delete/', views.ArticleDeleteView.as_view(), name="delete")

]