from tethys_sdk.base import TethysAppBase, url_map_maker

class App(TethysAppBase):
    """
    Tethys app class for Hello World.
    """
    name = 'Hello World'  # Human-readable app name
    description = 'Hello World Tethys app for demonstrating map and GeoJSON fetching from S3.'
    package = 'hello_world'  # WARNING: Do not change this value
    index = 'hello_world:home'
    icon = f'{package}/images/icon.gif'
    root_url = 'hello-world'  # URL prefix for the app
    color = '#00FFFF'
    tags = 'Water Demand, WRLU, Residential Irrigation, Hydrology, Water Management, Planning Tools, Decision Support, Utah'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Define URL mappings for the app.
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            # Home page (root of app)
            UrlMap(
                name='home',
                url='home',  # Root URL for the app
                controller='hello_world.controllers.home_page'
            ),

            # Map page
            UrlMap(
                name='map',
                url='map',  # Appends to root_url -> /apps/hello-world/map
                controller='hello_world.controllers.map_page'
            ),

            # GeoJSON endpoint (used by JS to fetch data dynamically)
            UrlMap(
                name='geojson',
                url='geojson',  # Appends to root_url -> /apps/hello-world/geojson
                controller='hello_world.controllers.serve_geojson'
            ),
        )

        return url_maps