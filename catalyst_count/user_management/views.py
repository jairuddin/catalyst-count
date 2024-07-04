from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from authentication_login.models import CustomUser
from .forms import CustomUserCreationForm
from django.http import HttpResponse

@login_required
def user_list(request):
    if request.user.is_staff or request.user.is_superuser:
        users = CustomUser.objects.all()
        return render(request, 'user_management_temp/users.html', {'users': users})
    else:
        return HttpResponse("<h2>The information is confidential.Only for Staff Users. <a href='/accounts/login/'>Back To Home</a></h2>")

@login_required
@staff_member_required
def user_delete(request, user_id):
    user = CustomUser.objects.get(id=user_id) 
    user.delete() 
    return redirect('user_list')

@login_required
@staff_member_required
def add_user(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("is_valid")
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('add_user')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'user_management_temp/users.html', {'form': form, 'users': CustomUser.objects.all()})

