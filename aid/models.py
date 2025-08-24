from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Request(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    category = ForeignKey('Category', on_delete=models.CASCADE)
    location = ForeignKey('aid.Location', on_delete=models.CASCADE)
    description = models.TextField()
    urgency_level = models.CharField(max_length=50, choices=URGENCY_CHOICES, default='medium')
    preferred_time = models.CharField(max_length=50, blank=True, null=True)
    estimated_duration = models.CharField(max_length=50, blank=True, null=True)
    skills = models.CharField(max_length=50, blank=True, null=True)
    offer = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='requests_pictures/', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    time_posted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.title
    
    @property
    def responses(self):
        """Property to get responses for this request"""
        # This assumes you have a Response model or similar
        # Return an empty queryset for now
        from django.db.models import QuerySet
        return QuerySet(model=None).none()

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name