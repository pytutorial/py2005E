from django.shortcuts import render, HttpResponse
import json

def index(request):
    return render(request, 'index.html')

def hello(request): #127.0.0.1:8000/hello
    content = json.dumps({'message': 'hello'})
    return HttpResponse(content, content_type='application/json')  

products = [
    {'code': 'IPX', 'name': 'Iphone X', 'price': 17.5},
    {'code': 'IP8', 'name': 'Iphone 8', 'price': 12.5},
    {'code': 'IP7', 'name': 'Iphone 7', 'price': 8.5},
]      

#http://127.0.0.1:8000/search_product?keyword=IPX
def searchProduct(request):
    keyword = request.GET.get('keyword', '')
    result = [p for p in products if keyword in p['code']
                        or keyword in p['name']]
    return HttpResponse(json.dumps(result)
                    , content_type='application/json')
