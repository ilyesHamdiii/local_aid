from django.contrib import admin
from django.urls import path,include
from .views import login_view,register_view,logout_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'
urlpatterns = [
    path('login',login_view, name='login'),  
    path('register',register_view, name='register'),
    path('logout', logout_view, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
