from django.urls import path
from .views import *

urlpatterns =[
    path('', index, name='home'),    
    path('add_category', addCategory, name='add-category'),
    path('update_category/<pk>', updateCategory, name='update-category'),
    path('delete_category/<pk>', deleteCategory, name='delete-category'),
    path('list_product', listProduct, name='list-product'),
    path('create_product', createProduct, name='create-product'),
    path('update_product/<pk>', updateProduct, name='update-product'),
    path('delete_product/<pk>', deleteProduct, name='delete-product'),

]