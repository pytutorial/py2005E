from rest_framework.decorators import api_view
from rest_framework.response import Response
#http://127.0.0.1:8000/api/hello

productList = [
    {'id': 1, 'code': 'IP7', 'name': 'IPhone 7'},
    {'id': 2, 'code': 'IP8', 'name': 'IPhone 8'},
]

@api_view(['GET'])
def searchProduct(request):#127.0.0.1:8000/api/search_product
    name = request.GET.get('name', '')
    result = [p for p in productList if name in p['name']]
    return Response(result)

@api_view(['POST'])
def createProduct(request):
    code = request.data.get('code', '')
    name = request.data.get('name', '')
    id = len(productList) + 1
    productList.append({'id':id, 'code': code, 'name': name})
    return Response({'success': True})

@api_view(['PUT'])
def updateProduct(request, pk):
    for p in productList:
        if p['id'] == int(pk):
            p['code'] = request.data.get('code', '')
            p['name'] = request.data.get('name', '')
            return Response({'success', True})
    return Response({'success': False, 'error': 'Not found'})


@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

# Create your views here.
