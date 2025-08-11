from django.contrib import admin
from django.urls import path, include
from aid.models import Request, Category, Location


admin.site.register(Request)
admin.site.register(Category)
admin.site.register(Location)
""" admin.site.register(UserTable) """

# Register your models here.
