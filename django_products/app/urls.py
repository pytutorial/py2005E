from django.urls import path
from .views import *

urlpatterns =[
    path('', index, name='home'),    
    path('add_category', addCategory, name='add-category'),
    path('update_category/<pk>', updateCategory, name='update-category'),
    path('delete_category/<pk>', deleteCategory, name='delete-category'),

]