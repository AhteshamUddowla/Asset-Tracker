from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Asset

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('assets')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('assets')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')


def assets_view(request):
    assets = Asset.objects.all()
    return render(request, 'assets/assets.html', {'assets':assets})