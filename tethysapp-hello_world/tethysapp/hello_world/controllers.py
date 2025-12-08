from django.shortcuts import render

def home_page(request):
    """Home page view"""
    return render(request, 'hello_world/home.html')

def map_page(request):
    """Map and plot page view"""
    return render(request, 'hello_world/map.html')