from django.contrib import admin
from django.urls import path
from . import views

app_name = 'MyBestRun'

urlpatterns = [
    path('', views.front, name='front'),
    path('signup/', views.signupview, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('formcalendar/', views.FormCalendar.as_view(), name='formcalendar'),
    path(
        'formcalendar/<int:year>/<int:month>/<int:day>/', views.FormCalendar.as_view(), name='formcalendar'
    ),
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/',
        views.MyCalendar.as_view(), name='mycalendar'),
]
