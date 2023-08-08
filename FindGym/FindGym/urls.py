from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('gyms.urls')),
    path('users/', include('users.urls')),
    path("admin/", admin.site.urls) 
]
