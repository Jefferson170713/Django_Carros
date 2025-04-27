from django.shortcuts import render
from django.contrib.auth import UserCreationForm

def register_view(request):
    user_form = UserCreationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})
