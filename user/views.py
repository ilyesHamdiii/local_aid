from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from . import models 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib import messages

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