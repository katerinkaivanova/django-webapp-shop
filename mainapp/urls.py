from django.urls import path

import mainapp.views as mainapp

app_name = 'main_app'

urlpatterns = [
   path('', mainapp.products_view, name='index'),
   path('<int:pk>/', mainapp.products_view, name='category'),
]