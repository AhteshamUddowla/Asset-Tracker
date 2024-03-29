from django.shortcuts import render
from .models import Asset

# Create your views here.
def assets(request):
    assets = Asset.objects.all()
    return render(request, 'assets/assets.html', {'assets':assets})