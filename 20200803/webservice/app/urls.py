#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('hello', hello),
    path('search_product', searchProduct),
]