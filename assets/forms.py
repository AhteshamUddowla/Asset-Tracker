from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, Asset

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AccountForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_no', 'company', 'job_title']

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'