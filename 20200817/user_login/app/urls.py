#app/urls.py
from django.urls import path
from .views import *
from django.urls import include
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index),
]