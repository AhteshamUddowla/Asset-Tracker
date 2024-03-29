from django.contrib import admin
from .models import Asset, CustomUser, Company, Employee

# Register your models here.
admin.site.register(Asset)
admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(Employee)