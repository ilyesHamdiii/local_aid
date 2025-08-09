from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Request(models.Model):
    title= models.CharField(max_length=200)
    category=ForeignKey('Category', on_delete=models.CASCADE)
    location=ForeignKey('aid.Location', on_delete=models.CASCADE)
    description=models.TextField()
    urgency_level=models.CharField(max_length=50)
    preferred_time=models.CharField( max_length=50)
    estimated_duration=models.CharField(max_length=50)
    offer=models.TextField()
    photo=models.ImageField(upload_to='request_photos/', blank=True, null=True)
    author=models.ForeignKey('user.UserTable', on_delete=models.CASCADE) 
    time_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
class Location(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
