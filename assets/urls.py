from django.urls import path
from . import views

urlpatterns = [
    path('', views.assets_view, name='assets'),
    path('login/', views.login_view, name='login'),
]