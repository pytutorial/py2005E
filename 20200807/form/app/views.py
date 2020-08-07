from django.shortcuts import render, redirect
from .forms import *
def index(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            context = {
                'fullname': form.cleaned_data['fullname'],
                'phone': form.cleaned_data['phone'],
            }
            return render(request, 'confirm.html', context)
    context = {'form': form}
    return render(request, 'index.html', context)

def listProduct(request):    
    productList = Product.objects.all()
    context = {'productList': productList}
    return render(request, 'product/list.html', context)
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')

    context = {'form' : form}
    return render(request, 'product/form.html', context)    

def updateProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES
                            ,instance=product)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    context = {'form': form}
    return render(request, 'product/form.html', context)