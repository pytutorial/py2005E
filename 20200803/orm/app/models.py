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

if getProductList().count() == 0:
    addProduct('IPX', 'IPhone X', 17.5)
    addProduct('IP8', 'IPhone 8', 12.5)
    addProduct('IP7', 'IPhone 7', 8.5)

for p in getProductList():
    print(p.code, p.name, p.price)    