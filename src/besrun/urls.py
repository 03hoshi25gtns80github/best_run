from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyBestRun.urls')),
    path('accounts/', include('allauth.urls')),
]

