from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'        

class OrderForm(forms.Form):
    qty = forms.IntegerField(min_value=1)
    fullname = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()  

class SearchForm(forms.Form):
    name = forms.CharField(required=False)
    category = forms.ModelChoiceField(required=False,
        queryset=Category.objects.all()) 
    PRICE_CHOICES = [
        ('', 'Tất cả'),
        (1, 'Dưới 10 triệu'),
        (2, 'Từ 10 đến 20 triệu'),
        (3, 'Trên 20 triệu')
    ]     
    priceRange = forms.ChoiceField(required=False,
        choices=PRICE_CHOICES)