from django.shortcuts import render, redirect
from .forms import *

def listCategory(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html',
             {'categoryList': categoryList})

def addCategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-category')

    return render(request, 'category/form.html', {'form': form})

def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list-category')

    return render(request, 'category/form.html', {'form': form})

def deleteCategory(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('list-category')

def listProduct(request): #http://localhost:8000/list_product
    context = {'productList': Product.objects.all()}
    return render(request, 'product/list.html', context)

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')

    return render(request, 'product/form.html', {'form': form})    

def updateProduct(request, pk):
    p = Product.objects.get(pk=pk)
    form = ProductForm(instance=p)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid(): 
            form.save()
            return redirect('list-product')
    return render(request, 'product/form.html', {'form': form})

def deleteProduct(request, pk):
    p = Product.objects.get(pk=pk)
    p.delete()
    return redirect('list-product')    
