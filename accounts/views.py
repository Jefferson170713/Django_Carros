from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:login')
    else:
        user_form = UserCreationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cars:cars_index')
    else:
        login_form = AuthenticationForm()
    return render( request, 'accounts/login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

