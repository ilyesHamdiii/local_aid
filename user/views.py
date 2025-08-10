from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password, make_password
from .models import UserTable
from aid.models import Location

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = UserTable.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                messages.success(request, "Logged in successfully.")
                return redirect("aid:requests")
            else:
                messages.error(request, "Invalid email or password.")
        except UserTable.DoesNotExist:
            messages.error(request, "Invalid email or password.")
    return render(request, "user/login.html")

def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        location_id = request.POST.get("location")
        phone_number = request.POST.get("phone_number")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif UserTable.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            try:
                location = Location.objects.get(id=location_id)
            except Location.DoesNotExist:
                messages.error(request, "Invalid location selected.")
                return render(request, "user/register.html")
            user = UserTable(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password),
                location=location,
                phone_number=phone_number,                
            )
            user.save()
            print("User saved:", user)
            request.session['user_id'] = user.id
            messages.success(request, "Registration successful.")
            return redirect("aid:requests")
    # Pass locations to the template for the dropdown
    locations = Location.objects.all()
    return render(request, "user/register.html", {"locations": locations})

def logout_view(request):
    logout(request)
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return render(request, 'user/logout.html')