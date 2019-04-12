from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products_view, name='index'),
   path('category/<int:pk>/', mainapp.products_view, name='category'),
]