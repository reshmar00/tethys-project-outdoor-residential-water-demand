import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from tethys_sdk.routing import controller

# Path to the app directory
APP_DIR = os.path.dirname(os.path.abspath(__file__))

@controller(name="home")
def home_page(request):
    """
    Renders the main home page template.
    """
    return render(request, 'hello_world/home.html')


@controller(name="map")
def map_page(request):
    """
    Renders the dedicated map page template.
    """
    return render(request, 'hello_world/map.html')


@controller(name="geojson")
def serve_geojson(request, feature_file=None):
    """
    Serve GeoJSON files from the app's resources folder.
    
    If 'feature_file' is provided, it will look in resources/GeoJSON/Features/.
    Otherwise, it will look in resources/GeoJSON/ for a default GeoJSON.
    """
    # Default GeoJSON file if none specified
    default_geojson = 'WaterRelatedLandUse2010to2015_5951885296121871261.geojson'

    if feature_file:
        GEOJSON_PATH = os.path.join(APP_DIR, 'resources', 'GeoJSON', 'Features', feature_file)
    else:
        GEOJSON_PATH = os.path.join(APP_DIR, 'resources', 'GeoJSON', default_geojson)

    if not os.path.exists(GEOJSON_PATH):
        return JsonResponse({"error": f"GeoJSON file not found: {GEOJSON_PATH}"}, status=404)

    with open(GEOJSON_PATH, 'r') as f:
        data = json.load(f)

    return JsonResponse(data)