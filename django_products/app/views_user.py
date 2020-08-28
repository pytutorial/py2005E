from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from datetime import datetime

def index(request):
    productList = Product.objects.all()
    context = {'productList': productList}
    return render(request, 'user/index.html', context)

def viewProduct(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'user/view_product.html', context)

def saveOrder(product, data):
    order = Order()
    order.product = product
    order.priceUnit = product.price
    order.qty = data['qty']
    order.fullname = data['fullname']
    order.phone = data['phone']
    order.address = data['address']
    order.orderDate = datetime.now()
    order.status = Order.OrderStatus.PENDING
    order.save()

def orderProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = OrderForm(initial={'qty': 1})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            saveOrder(product, form.cleaned_data)
            return redirect('/thank_you')
    context = {'product': product, 'form': form}
    return render(request,'user/order_product.html', context)

def thankYou(request):
    return render(request, 'user/thank_you.html')    