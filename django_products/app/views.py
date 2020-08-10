from django.shortcuts import render, redirect
from .forms import *

def index(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html', {'categoryList': categoryList})

def addCategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'category/form.html', {'form': form})
