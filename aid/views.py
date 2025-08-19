from django.shortcuts import render, redirect, get_object_or_404
from .models import Request, Category, Location
from django.core.paginator import Paginator
from user.models import UserProfile
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.contrib import messages


def base_view(request):
    if not request.user.is_authenticated:
        return redirect("user:login")
    nb = Request.objects.filter(author=request.user).first()
    profile = UserProfile.objects.filter(user=request.user).first()
    print("profile", profile)
    return render(request, 'aid/base.html', {"profile": profile})

def home_view(request):
    return render(request, "aid/home.html")

def request_detail_view(request, request_id):
    try:
        request_detail = Request.objects.get(id=request_id)
    except Request.DoesNotExist:
        return render(request, 'aid/request_not_found.html', {'request_id': request_id})
    profile=UserProfile.objects.filter(user=request_detail.author).first()
    context = {
        'request': request_detail,
        "profile":profile
    }
    return render(request, 'aid/request_detail.html', context)

def request_not_found_view(request, request_id):
    context = {
        'request_id': request_id,
    }
    return render(request, 'aid/request_detail.html')

def post_request_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        location = request.POST.get('location')
        urgency_level = request.POST.get('urgency', 'medium')  # Default to medium
        preferred_time = request.POST.get('preferred-time')
        estimated_duration = request.POST.get('duration')
        offer = request.POST.get('compensation')
        photo = request.FILES.get('photos')
        author = request.user

        # Validate required fields
        if not all([title, description, category, location]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'aid/post_request.html')

        try:
            # Get the actual model instances
            category_obj = Category.objects.get(id=category)
            location_obj = Location.objects.get(id=location)
            
            post = Request.objects.create(
                title=title,
                description=description,
                category=category_obj,
                location=location_obj,
                urgency_level=urgency_level,
                preferred_time=preferred_time,
                estimated_duration=estimated_duration,
                offer=offer,
                photo=photo,
                author=author,
                status='open'  # Set default status
            )
            post.save()
            messages.success(request, 'Request posted successfully!')
            return redirect('aid:my_requests')
        except (Category.DoesNotExist, Location.DoesNotExist) as e:
            messages.error(request, 'Invalid category or location selected.')
            return render(request, 'aid/post_request.html')
    
    # Get categories and locations for the form
    categories = Category.objects.all()
    locations = Location.objects.all()
    context = {
        'categories': categories,
        'locations': locations,
    }
    return render(request, 'aid/post.html', context)

def requests(request):
    requests = Request.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    profile = UserProfile.objects.filter(user=request.user).first()
    context = {
        'requests': requests,
        'categories': categories,
        'locations': locations,
        "profile": profile
    }
    print(categories)
    print("context",context)
    return render(request, 'aid/requests.html', context)

def requests_list(request):
    requests = Request.objects.all().order_by('-time_posted')
    paginator = Paginator(requests, 6)  # 6 requests per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'aid/requests.html', {'page_obj': page_obj})

@login_required
def edit_request(request, request_id):
    req = get_object_or_404(Request, id=request_id, author=request.user)
    
    if request.method == 'POST':
        # Update the request with new data
        req.title = request.POST.get('title', req.title)
        req.description = request.POST.get('description', req.description)
        
        category_id = request.POST.get('category')
        if category_id:
            try:
                req.category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                pass
                
        location_id = request.POST.get('location')
        if location_id:
            try:
                req.location = Location.objects.get(id=location_id)
            except Location.DoesNotExist:
                pass
                
        req.urgency_level = request.POST.get('urgency', req.urgency_level)
        req.preferred_time = request.POST.get('preferred-time', req.preferred_time)
        req.estimated_duration = request.POST.get('duration', req.estimated_duration)
        req.offer = request.POST.get('compensation', req.offer)
        req.status=request.POST.get('status',req.status)
        
        photo = request.FILES.get('photos')
        if photo:
            req.photo = photo
            
        req.save()
        messages.success(request, 'Request updated successfully!')
        return redirect('aid:my_requests')
    
    categories = Category.objects.all()
    locations = Location.objects.all()
    context = {
        'request': req,
        'categories': categories,
        'locations': locations,
    }
    return render(request, 'aid/edit_request.html', context)

@login_required
def delete_request(request, request_id):
    if request.method == 'POST':
        req = get_object_or_404(Request, id=request_id, author=request.user)
        req.delete()
        messages.success(request, 'Request deleted successfully.')
        return redirect('aid:my_requests')
    return redirect('aid:my_requests')

@login_required
def my_requests(request):   
    user_requests = Request.objects.filter(author=request.user).order_by('-time_posted')
    
    # Calculate stats
    total_requests = user_requests.count()
    open_requests = user_requests.filter(status='open').count()
    completed_requests = user_requests.filter(status='closed').count()
    total_responses = 0  # You'll need to implement this based on your response model
    
    context = {
        "user_requests": user_requests,
        "total_requests": total_requests,
        "open_requests": open_requests,
        "completed_requests": completed_requests,
        "total_responses": total_responses,
    }
    return render(request, "aid/my_requests.html", context)