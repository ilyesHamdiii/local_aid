from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
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
from aid.models import Request
from conversation.models import Conversation

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
@login_required
def my_requests(request):   
    user_requests = Request.objects.filter(author=request.user).order_by('-time_posted')
    
    # Calculate stats
    total_requests = user_requests.count()
    open_requests = user_requests.filter(status='open').count()
    completed_requests = user_requests.filter(status='completed').count()
    total_responses = 0  # You'll need to implement this based on your response model
    
    context = {
        "user_requests": user_requests,
        "total_requests": total_requests,
        "open_requests": open_requests,
        "completed_requests": completed_requests,
        "total_responses": total_responses,
    }
    return render(request, "aid/my_requests.html", context)
@login_required

def profile_user_view(request, request_author):
    """View for displaying user profiles"""
    from django.contrib.auth.models import User
    from django.shortcuts import get_object_or_404
    pid=User.objects.filter(username=request_author).first()
    """ req=Request.objects.filter(id=pid).firs() """
    conversations = Conversation.objects.filter(members=[pid.id]).filter(members__in=[request.user.id])
    print("conversation :",conversations.id)
    
    profile_user = get_object_or_404(UserProfile, user=pid.id)
    
    # Get user's requests (limit to recent 3 for display)
    user_requests = Request.objects.filter(author=pid.id).order_by('-time_posted')[:3]
    
    # Calculate user stats
    total_requests = Request.objects.filter(author=pid.id).count()
    total_helps = 0  # You'll need to implement this based on your response/help model
    rating = 5.0  # You'll need to implement this based on your review model
    member_since = request.user.date_joined.year
    
    # Get reviews (you'll need to create a Review model)
    user_reviews = []  # Placeholder for actual reviews
    
    user_stats = {
        'total_requests': total_requests,
        'total_helps': total_helps,
        'rating': rating,
        'member_since': member_since,
    } 
    
    context = {
        'profile_user': profile_user,
        'user_requests': user_requests,
        'user_reviews': user_reviews,
        'user_stats': user_stats,
        "conversation":conversations
    }
    
    return render(request,"user/profile_view.html",context)