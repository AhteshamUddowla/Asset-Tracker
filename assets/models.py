from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.username)
    
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Employee(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     job_title = models.CharField(max_length=20, null=True, blank=True)

#     def __str__(self):
#         return self.user.username

class Asset(models.Model):
    ASSET_TYPES = [
        ('Phone', 'Phone'),
        ('Tablet', 'Tablet'),
        ('Laptop', 'Laptop'),
        ('PC', 'PC')
    ]

    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPES)
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    assigned_date = models.DateField(null=True, blank=True)
    returned_date = models.DateField(null=True, blank=True)
    assigned_condition = models.CharField(max_length=100, null=True, blank=True)
    returned_condition = models.CharField(max_length=100, null=True, blank=True)
    assigned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asset_type} - {self.id}"
    
