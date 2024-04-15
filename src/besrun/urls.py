from django.contrib import admin
from django.urls import path
from MyBestRun.views import front, signupview, loginview, best_run_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front, name='front'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('best_run_form/', best_run_form, name='best_run_form'),
]
