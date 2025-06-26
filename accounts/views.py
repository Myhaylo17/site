from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # ← додаємо
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, LoginForm
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Невірний логін або пароль')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')

@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required(login_url='/login/')
def achievments_view(request):
    return render(request, 'accounts/achievments.html')

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('login')  # або просто перенаправлення


