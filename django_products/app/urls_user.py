from django.urls import path
from .views_user import *

urlpatterns =[
    path('', index, name='home'),    
    path('view_product/<pk>', viewProduct),
    path('order_product/<pk>', orderProduct),
    path('thank_you', thankYou),
]