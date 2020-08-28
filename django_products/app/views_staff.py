from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def listCategory(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html',
             {'categoryList': categoryList})

@login_required
def addCategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-category')

    return render(request, 'category/form.html', {'form': form})

@login_required
def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list-category')

    return render(request, 'category/form.html', {'form': form})

@login_required
def deleteCategory(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('list-category')

@login_required
def listProduct(request): #http://localhost:8000/list_product
    context = {'productList': Product.objects.all()}
    return render(request, 'product/list.html', context)

@login_required
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')

    return render(request, 'product/form.html', {'form': form})    

@login_required
def updateProduct(request, pk):
    p = Product.objects.get(pk=pk)
    form = ProductForm(instance=p)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid(): 
            form.save()
            return redirect('list-product')
    return render(request, 'product/form.html', {'form': form})

@login_required
def deleteProduct(request, pk):
    p = Product.objects.get(pk=pk)
    p.delete()
    return redirect('list-product')    

@login_required
def listOrder(request):
    orderList = Order.objects.all()
    context = {'orderList': orderList}
    return render(request, 'order/list.html', context)

@login_required
def viewOrder(request, pk):
    order = Order.objects.get(pk=pk)
    context = {'order': order}
    return render(request, 'order/detail.html', context)    