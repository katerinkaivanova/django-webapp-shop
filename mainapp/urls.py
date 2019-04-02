from django.urls import path

from mainapp.views import products_view

urlpatterns = [
   path('', products_view, name='index'),
   path('<int:pk>/', products_view, name='category'),
]