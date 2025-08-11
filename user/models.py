from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import AbstractUser

""" # Create your models here.
class UserTable():
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    location = models.ForeignKey('aid.Location', on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # or any other required fields

    def __str__(self):
        return f"{self.first_name} {self.last_name}" """