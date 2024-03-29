from django.db import models

# Create your models here.
class Asset(models.Model):
    ASSET_TYPES = [
        ('Phone', 'Phone'),
        ('Tablet', 'Tablet'),
        ('Laptop', 'Laptop'),
        ('PC', 'PC')
    ]

    asset_type = models.CharField(max_length=20, choices=ASSET_TYPES)
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    assigned_date = models.DateField(null=True, blank=True)
    returned_date = models.DateField(null=True, blank=True)
    assigned_condition = models.CharField(max_length=100, null=True, blank=True)
    returned_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.asset_type} - {self.id}"
    
