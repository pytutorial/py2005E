#app/url.py
from django.urls import path
from .views_api import *

urlpatterns = [
    path('get_root_category_list', getRootCategoryList),
    path('get_sub_category_list/<pk>', getSubCategoryList),
    path('hello2', HelloView.as_view()),
    path('hello', hello)
]