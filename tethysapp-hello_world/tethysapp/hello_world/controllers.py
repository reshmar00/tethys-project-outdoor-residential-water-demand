from django.shortcuts import render

def home_page(request):
    """Home page with map and chart"""
    return render(request, 'hello_world/home.html')