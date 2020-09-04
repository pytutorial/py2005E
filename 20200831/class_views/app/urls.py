#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('list_product', ProductListView.as_view()),
    path('create_product', ProductCreateView.as_view())
]