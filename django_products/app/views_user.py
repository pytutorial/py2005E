from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, SearchForm
from datetime import datetime
import math

def getPriceRangeValue(priceRange):
    if str(priceRange) == '1': return None, 10
    if str(priceRange) == '2': return 10, 20
    if str(priceRange) == '3': return 20, None
    return None, None

def searchProduct(data):
    name = data.get('name')
    categ = data.get('category')
    priceRange = data.get('priceRange')
    productList = Product.objects.all()
    if name:
        productList = productList.filter(name__contains=name)
    if categ:
        productList = productList.filter(category__id=categ)
    
    minPrice, maxPrice = getPriceRangeValue(priceRange)
    if minPrice:
        productList = productList.filter(price__gte=minPrice*1e6)
    if maxPrice:
        productList = productList.filter(price__lte=maxPrice*1e6)
    
    return productList    

def createQueryString(data):
    name = data.get('name', '')
    category = data.get('category', '')
    priceRange = data.get('priceRange', '')
    return f'/?name={name}&category={category}&priceRange={priceRange}'

def index(request):
    PAGE_SIZE = 3
    form = SearchForm(request.GET)
    productList = searchProduct(request.GET)

    page = int(request.GET.get('page', 1))
    start = (page-1)*PAGE_SIZE
    end = page*PAGE_SIZE
    total = len(productList)
    num_page = math.ceil(total/PAGE_SIZE)
   
    context = {
        'productList': productList[start:end],
        'total': total,
        'num_page': num_page,
        'page': page, 
        'next_page': page + 1 if page < num_page else None,
        'prev_page': page - 1 if page > 1 else None,
        'form': form,
        'query_str': createQueryString(request.GET),
        }
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