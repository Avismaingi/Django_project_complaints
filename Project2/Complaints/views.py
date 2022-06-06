from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
     return render(request, "home.html")

def login_user(request):
     return render(request, "login_user.html")

def login_admin(request):
     return render(request, "login_admin.html")