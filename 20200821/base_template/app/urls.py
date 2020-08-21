#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('page2', page2),
    path('page3', page3),
]