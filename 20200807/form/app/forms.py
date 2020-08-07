#app/forms.py
from django import forms
from .models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ('code', 'name', 'price')
        #exclude = ('image',)

class CustomerForm(forms.Form):
    fullname = forms.CharField(max_length=50, label='Họ tên')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=20, label='Số điện thoại')
    address = forms.CharField(max_length=200, label='Địa chỉ'
                            , widget=forms.Textarea
                            , required=False)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if not phone.isdigit() or phone[0] != '0':
            raise forms.ValidationError(
                        'Số điện thoại không hợp lệ')
        return phone

