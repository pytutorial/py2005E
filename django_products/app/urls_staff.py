from django.urls import path
from .views_staff import *
from django.urls import include

urlpatterns =[
    path('accounts/', include('django.contrib.auth.urls')),
    path('staff', listCategory, name='list-category'),
    path('add_category', addCategory, name='add-category'),
    path('update_category/<pk>', updateCategory, name='update-category'),
    path('delete_category/<pk>', deleteCategory, name='delete-category'),
    path('list_product', listProduct, name='list-product'),
    path('create_product', createProduct, name='create-product'),
    path('update_product/<pk>', updateProduct, name='update-product'),
    path('delete_product/<pk>', deleteProduct, name='delete-product'),

    path('list_order', listOrder),
    path('view_order/<pk>', viewOrder),
]