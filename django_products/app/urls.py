from django.urls import path
from .views import *

urlpatterns =[
    path('', index, name='home'),    
    path('add_category', addCategory, name='add-category'),
]