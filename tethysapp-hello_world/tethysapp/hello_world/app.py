from tethys_sdk.base import TethysAppBase
from tethys_sdk.base import url_map_maker

class App(TethysAppBase):
    """
    Tethys app class for Hello World.
    """
    name = 'Hello World'
    description = ''
    package = 'hello_world'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'hello-world'
    color = '#00FFFF'
    tags = 'Water Demand,WRLU,Residential Irrigation,Hydrology,Water Management,Planning Tools,Decision Support,Utah'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        UrlMap = url_map_maker(self.root_url)
        url_maps = (
            # Home page
            UrlMap(
                name='home',
                url='',
                controller='hello_world.controllers.home_page'
            ),
            # Map page
            UrlMap(
                name='map',
                url='hello-world/map',
                controller='hello_world.controllers.map_page'
            ),
            # GeoJSON endpoint
            UrlMap(
                name='geojson',
                url='geojson',
                controller='hello_world.controllers.serve_geojson'
            ),
        )
        return url_maps