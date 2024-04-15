from django.contrib import admin
from django.urls import path
from MyBestRun.views import signup, front

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('', front, name='front'),
]
