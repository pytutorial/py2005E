from django.shortcuts import render
from .forms import *
def index(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            return render('thankyou.html')
    context = {'form': form}
    return render(request, 'index.html', context)
