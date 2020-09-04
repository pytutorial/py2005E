from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, TemplateView, View
from .models import *
from django import forms
# Create your views here.
def index(request):
    name = request.GET.get('name', '')
    productList = Product.objects.filter(name__contains=name)
    context = {'productList' : productList, 'name': name}
    return render(request, 'index.html', context)

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
    context_object_name = 'productList'
    paginate_by = 10

    def get_queryset(self):
        name = self.request.GET.get('name', '')
        return Product.objects.filter(name__contains=name)
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['name']  = self.request.GET.get('name')
        return context
        

class ProductCreateView(CreateView):    
    template_name = 'product_form.html'
    success_url = '/'
    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = '__all__'

    def get(self, request, *args, **kargs):
        form = self.ProductForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kargs):
        #pk = kargs['pk']   
        form = self.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = {'form': form}
        return render(request, self.template_name, context)


    
