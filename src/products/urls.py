from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.product_detail_view, name='detail'),
    path('create/', views.product_create_view, name ='create'),
    path('<int:id>/delete/', views.products_delete_view, name='delete'),
    path('', views.products_list_view, name ='list')

]