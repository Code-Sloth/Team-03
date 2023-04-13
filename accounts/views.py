from django.shortcuts import render, redirect
from .forms import CustomUserAuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('')
    else:
        form = CustomUserAuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html',context)
