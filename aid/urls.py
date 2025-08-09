from django.contrib import admin
from django.urls import path,include
from .views import base_view, home_view, request_detail_view, post_request_view, requests
from django.conf import settings
from django.conf.urls.static import static

app_name = 'aid'
urlpatterns = [
    path("",base_view), # Include the URLs from the aid app
    path("home/", home_view, name="home"),
    path("request_detail/", request_detail_view, name="request_detail"),
    path("requests/", requests, name="requests"),
    path("post/", post_request_view, name="post_request"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
