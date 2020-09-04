#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('hello', hello),
    path('create_product', createProduct),
    path('update_product/<pk>', updateProduct),
    path('search_product', searchProduct),
]