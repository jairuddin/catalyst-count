from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('account_login')  
    else:
        form = UserCreationForm() 
    return render(request, {'form': form}) 

def login(request):
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request, user) 
            return redirect('/')  
    else:
        form = AuthenticationForm() 
    return render(request, {'form': form}) 


