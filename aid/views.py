from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request, 'aid/base.html')
def home_view(request):
    return render(request, 'aid/home.html')
def request_detail_view(request):
    return render(request, 'aid/request_detail.html')
def post_request_view(request):
    return render(request, 'aid/post.html')
def requests(request):
    return render(request, 'aid/requests.html')