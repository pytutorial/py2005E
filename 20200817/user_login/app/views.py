from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
#from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

#127.0.0.1:8000/staff
#@login_required
@staff_member_required
def staffView(request):
    return render(request, 'staff.html')

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'],
                        password=request.POST['password1'])
            login(request, user) 
            return redirect('/')                               
    return render(request,'registration/signup.html', {'form': form})    

def index(request):
    return render(request, 'index.html')

