from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from . import models 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

# Create your views here.

app_name='user'
def login_view(request):
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            print("form is valid ")
            login(request, form.get_user())
            return redirect("aid:home")
        else:
             messages.error(request, "Invalid username or password.")
    else: 
        print("form is not valid ")
        form = AuthenticationForm()
    print("no request at all ")
    return render(request, "user/login.html", { "form": form })


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        password1 = request.POST.get("password1")
        if password1 and len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
        elif form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("aid:home")
        else:
            messages.error(request, form.errors)
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", { "form": form })

@login_required
def logout_view(request):
    logout(request)
    return redirect("aid:home")
@login_required
def profile_view(request):
    if request.method == "POST":
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.location = request.POST.get("location", user_profile.location)
        user_profile.phone_number = request.POST.get("phone_number", user_profile.phone_number)
        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']
        user_profile.save()
        messages.success(request, "Profile updated successfully.")
    else:
        user_profile = UserProfile.objects.get(user=request.user)
    return render(request, "user/profile.html", {"user": request.user, "profile": user_profile})
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()