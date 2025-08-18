from django.contrib import admin
from django.urls import path,include
from .views import  home_view, request_detail_view, post_request_view, requests_list,base_view,edit_request,delete_request,my_requests
from django.conf import settings
from django.conf.urls.static import static

app_name = 'aid'
urlpatterns = [
    path("base",base_view,name="base"),
    path("", home_view, name="home"),
    path("request_detail/<int:request_id>", request_detail_view, name="request_detail"),
    path("requests/", requests_list, name="requests"),
    path("post/", post_request_view, name="post_request"),
    path("",include('user.urls')), 
    path("conversation/", include('conversation.urls')),
    path("dashboard/", include('dashboard.urls')),
    path('edit/<int:request_id>', edit_request, name='edit_request'),
    path('request/<int:request_id>/delete/', delete_request, name='delete_request'),
    path('my-requests/', my_requests, name='my_requests'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
