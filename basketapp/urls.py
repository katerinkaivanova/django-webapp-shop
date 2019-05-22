from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket_view, name='view'),
    path('add/<int:pk>/', basketapp.basket_add_view, name='add'),
    path('remove/<int:pk>)/', basketapp.basket_remove_view, name='remove'),
    path('update/<int:pk>/<int:quantity>/', basketapp.basket_update_view, name='update')
]
