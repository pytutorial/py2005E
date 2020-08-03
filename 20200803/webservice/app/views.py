from django.shortcuts import render, HttpResponse
import json

def index(request):
    return render(request, 'index.html')

def hello(request): #127.0.0.1:8000/hello
    content = json.dumps({'message': 'hello'})
    return HttpResponse(content, content_type='application/json')    
