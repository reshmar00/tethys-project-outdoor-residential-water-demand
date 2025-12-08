from tethys_sdk.base import controller
from django.shortcuts import render

@controller(name='home')
def home_page(request):
    return render(request, 'hello_world/home.html')

@controller(name='map')
def map_page(request):
    """
    Render simple page with map and plot.
    """
    return render(request, 'hello_world/map.html')