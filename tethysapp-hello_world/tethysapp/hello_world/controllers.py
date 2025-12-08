import json
from django.shortcuts import render
from django.http import JsonResponse
from tethys_sdk.routing import controller
import boto3
from botocore.exceptions import ClientError

# ---------------------------
# S3 Configuration
# ---------------------------
S3_BUCKET = 'files-tethys'
S3_PREFIX_FEATURES = 'GeoJSON/Features/'
S3_PREFIX_DEFAULTS = 'GeoJSON/'

# Initialize boto3 S3 client
s3_client = boto3.client('s3')

# ---------------------------
# Year -> S3 key mapping
# ---------------------------
GEOJSON_MAPPING = {
    "1989-1999": f"{S3_PREFIX_DEFAULTS}WaterRelatedLandUse1989to1999_3698172706161627342.geojson",
    "2000-2005": f"{S3_PREFIX_DEFAULTS}WaterRelatedLandUse2000to2005_-3114777994287811750.geojson",
    "2005-2010": f"{S3_PREFIX_DEFAULTS}WaterRelatedLandUse2005to2010_-6659534034996230781.geojson",
    "2010-2015": f"{S3_PREFIX_DEFAULTS}WaterRelatedLandUse2010to2015_5951885296121871261.geojson",
    "2017": f"{S3_PREFIX_FEATURES}Water_Related_Land_Use_Statewide_2017_1_-481964617480833885.geojson",
    "2018": f"{S3_PREFIX_FEATURES}Water_Related_Land_Use_Statewide_2018_-8528321676228921133.geojson",
    "2019": f"{S3_PREFIX_FEATURES}WaterRelatedLandUse_2019_-8745672325075131226.geojson",
    "2020": f"{S3_PREFIX_FEATURES}Water_Related_Land_Use_(2020)_-1477212891426658517.geojson",
    "2021": f"{S3_PREFIX_FEATURES}Water_Related_Land_Use_(2021)_5176608505762981678.geojson",
    "2022": f"{S3_PREFIX_FEATURES}WaterRelatedLandUse_2022_3335239321074573090.geojson",
    "2023": f"{S3_PREFIX_FEATURES}WaterRelatedLandUse_2023_-8289506273020472750.geojson"
}

# Default fallback file
DEFAULT_GEOJSON = f"{S3_PREFIX_DEFAULTS}WaterRelatedLandUse2010to2015_5951885296121871261.geojson"


# ---------------------------
# Controllers
# ---------------------------

@controller(name="home")
def home_page(request):
    """Renders the main home page template."""
    return render(request, 'hello_world/home.html')


@controller(name="map")
def map_page(request):
    """Renders the dedicated map page template."""
    return render(request, 'hello_world/map.html')


@controller(name="geojson")
def serve_geojson(request):
    """
    Serve GeoJSON files from S3.

    Accepts a 'year' query parameter. If the year is not found,
    returns the default GeoJSON or a JSON error.
    """
    year = request.GET.get('year')

    # Determine which S3 key to fetch
    if year:
        s3_key = GEOJSON_MAPPING.get(year)
        if not s3_key:
            # If year not mapped, return 404 JSON
            return JsonResponse({"error": f"No GeoJSON mapping found for year: {year}"}, status=404)
    else:
        # No year provided, use default file
        s3_key = DEFAULT_GEOJSON

    # Fetch from S3
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET, Key=s3_key)
        data = json.loads(response['Body'].read().decode('utf-8'))
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'NoSuchKey':
            return JsonResponse({"error": f"GeoJSON file not found in S3: {s3_key}"}, status=404)
        else:
            return JsonResponse({"error": f"S3 error: {str(e)}"}, status=500)
    except Exception as e:
        return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    return JsonResponse(data)