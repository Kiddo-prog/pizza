from distutils.log import Log
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Account created successfully')
            return redirect('user:login')
    else:
        form = UserRegistrationForm()
        messages.error(request, 'Error creating account. Try again later')
    return render(request, 'accounts/register.html', {'form': form})

class LoginUser(LoginView):
    template_name = 'accounts/login.html'

class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'