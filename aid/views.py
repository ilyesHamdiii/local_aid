from django.shortcuts import render,redirect
from .models import Request, Category, Location
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    return render(request, 'aid/home.html')
def request_detail_view(request,request_id):
    try:
        request_detail = Request.objects.get(id=request_id)
    except Request.DoesNotExist:
        return render(request, 'aid/request_not_found.html', {'request_id': request_id})
    context = {
        'request': request_detail,}
    return render(request, 'aid/request_detail.html', context)
def request_not_found_view(request, request_id):
    context = {
        'request_id': request_id,
    }


    return render(request, 'aid/request_detail.html')
def post_request_view(request):
    if request.method == 'POST':
        title= request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        location = request.POST.get('location')
        urgency_level = request.POST.get('urgency')
        preferred_time = request.POST.get('preferred-time')
        estimated_duration = request.POST.get('duration')
        offer = request.POST.get('compensation')
        photo = request.FILES.get('photos')
        author = request.user

        post=Request.objects.create(
            title=title,
            description=description,
            category_id=category,
            location_id=location,
            urgency_level=urgency_level,
            preferred_time=preferred_time,
            estimated_duration=estimated_duration,
            offer=offer,
            photo=photo,
            author=author
        )
        post.save()
        return redirect('aid:requests')
    return render(request, 'aid/post.html')

def requests(request):
    requests = Request.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    context = {
        'requests': requests,
        'categories': categories,
        'locations': locations
    }

    return render(request, 'aid/requests.html',context)

def requests_list(request):
    requests = Request.objects.all().order_by('-time_posted')
    paginator = Paginator(requests, 6)  # 6 requests per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'aid/requests.html', {'page_obj': page_obj})