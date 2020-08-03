from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()

def addProduct(code, name, price):
    product = Product(code=code, name=name, price=price)
    product.save()

def getProductList():
    return Product.objects.all()        
