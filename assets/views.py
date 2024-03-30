from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Asset
from .forms import CustomUserCreationForm, AccountForm

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

def signup_view(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'An error has occured')

    context = {'form':form}
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')

@login_required(login_url='login')
def assets_view(request):
    # filter by company so that one company can't see the assets of others
    company = request.user.customuser.company
    assigned_assets = Asset.objects.filter(company=company, assigned=True).order_by('id')
    unassigned_assets = Asset.objects.filter(company=company, assigned=False).order_by('id')
    context = {
        'assigned_assets': assigned_assets,
        'unassigned_assets': unassigned_assets,
    }
    return render(request, 'assets/assets.html', context)

@login_required(login_url='login')
def account_view(request):
    account = request.user.customuser
    form = AccountForm(instance=account)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('assets')
        
    context = {'form': form}
    return render(request, 'account.html', context)