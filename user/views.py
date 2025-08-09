from django.shortcuts import render




app_name = 'user'
# Create your views here.
def login_view(request):
    return render(request, 'user/login.html')
def register_view(request):
    return render(request, 'user/register.html')