#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('list_product', listProduct, name='list-product'),
    path('create_product', createProduct, name='create-product'),
    path('update_product/<pk>', updateProduct, name='update-product'),
]