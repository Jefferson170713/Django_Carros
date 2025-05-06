from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:login')
    else:
        user_form = UserCreationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})

