from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('Category', null=True, blank=True,
                 on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    def __str__(self):
        return self.name


