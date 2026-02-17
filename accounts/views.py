from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render (request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "admin":
            return render (request, 'home.html')
        else:
            return render (request, 'login.html', {"error": "Invalid username or password"})
    return render (request, 'login.html')

def dashboard(request):
    return render (request, 'dashboard.html')


