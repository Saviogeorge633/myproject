from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'accounts/signup.html')

def login_view(request):
    # ✅ If already logged in
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')  # ✅ important

    # ✅ THIS LINE WAS MISSING
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Create your views here.
