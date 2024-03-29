from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import CustomUser

def createCustomUser(sender, instance, created, **kwargs):
    if created:
        user = instance
        customuser = CustomUser.objects.create(
            user=user,
            username=user.username,
            email=user.email
        )

# when a user is created a custom user is also created using signals
post_save.connect(createCustomUser, sender=User)