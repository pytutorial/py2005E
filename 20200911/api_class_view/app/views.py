#app/views.py
from django.shortcuts import render
from .models import *
def index(request):
    rootCategoryList = Category.objects.filter(parent__isnull=True)
    context = {'rootCategoryList': rootCategoryList}
    return render(request, 'index.html', context)