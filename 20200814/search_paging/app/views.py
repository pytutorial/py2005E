from django.shortcuts import render
from django.db.models import Q
from .models import *
import math

def getPriceValueRange(priceRange):
    if priceRange == '': return None, None
    if priceRange == '1': return None, 10
    if priceRange == '2': return 10, 15
    if priceRange == '3': return 15, None    

def index(request):
    PAGE_SIZE = 5
    page = int(request.GET.get('page', 1))
    start = PAGE_SIZE*(page-1)
    end = start + PAGE_SIZE

    keyword = request.GET.get('keyword', '')
    priceRange = request.GET.get('priceRange', '')
    minPrice, maxPrice = getPriceValueRange(priceRange)
        
    productList = Product.objects.filter(
        Q(name__contains=keyword)|Q(code__contains=keyword))

    if minPrice:
        productList = productList.filter(price__gte=minPrice)

    if maxPrice:
        productList = productList.filter(price__lte=maxPrice)        

    total = len(productList)
    num_page = math.ceil(total/PAGE_SIZE)

    context = {
        'productList' : productList[start:end], 
        'keyword': keyword,
        'priceRange': priceRange,
        'start': start,
        'nextPage': page+1,
        'prevPage': page-1,
        'total': total,
        'num_page': num_page,
    }
    return render(request, 'index.html', context)
    #http://localhost:8000/?page=2

