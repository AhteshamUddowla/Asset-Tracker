from django.urls import path
from . import views

urlpatterns = [
    path('', views.assets_view, name='assets'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('account/', views.account_view, name='account'),
]