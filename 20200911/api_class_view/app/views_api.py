from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
#http://127.0.0.1:8000/api/hello
@api_view(['GET'])
def hello(requests):
    return Response({'message': 'Hello'})
#http://127.0.0.1:8000/api/hello2
class HelloView(APIView):
    def get(self, request):
        return Response({'message': "Hello - class based view"})  

    def post(self, request):
        name = request.data.get('name', '')
        return Response({'message': "Hello " + name})  

from .serializers import *

@api_view(['GET'])
def getRootCategoryList(request):
    categoryList = Category.objects.filter(parent__isnull=True)
    data = CategorySerializer(categoryList, many=True).data
    return Response(data)

@api_view(['GET'])
def getSubCategoryList(request, pk):
    categoryList = Category.objects.filter(parent__id=pk)
    data = CategorySerializer(categoryList, many=True).data
    return Response(data)


