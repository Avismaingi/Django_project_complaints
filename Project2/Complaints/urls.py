from django.contrib import admin
from django.urls import path, include
from Complaints import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login_user/', views.login_user, name='login'),
    path('login_admin/', views.login_admin, name='admin login'),
]
