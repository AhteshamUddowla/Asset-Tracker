from django.urls import path
from . import views

urlpatterns = [
    path('', views.assets_view, name='assets'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('account/', views.account_view, name='account'),
    path('add-asset/', views.add_asset_view, name='add-asset'),
    path('update-asset/<str:pk>/', views.update_asset_view, name='update-asset'),
    path('delete-asset/<str:pk>/', views.delete_asset_view, name='delete-asset'),
]