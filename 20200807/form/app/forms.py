#app/forms.py
from django import forms

class CustomerForm(forms.Form):
    fullname = forms.CharField(max_length=50, label='Họ tên')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=20, label='Số điện thoại')
    address = forms.CharField(max_length=200, label='Địa chỉ'
                            , widget=forms.Textarea)