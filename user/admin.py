from django.contrib import admin
from django.urls import path, include
from aid.models import Request, Category, Location
from .models import UserProfile


admin.site.register(Request)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(UserProfile)

""" admin.site.register(UserTable) """

# Register your models here.
