from django.urls import path

#from mainapp.views import products_view

import mainapp.views as mainapp

app_name = 'main_app'

urlpatterns = [
   path('', mainapp.products_view, name='index'),
   path('<int:pk>/', mainapp.products_view, name='category'),
]