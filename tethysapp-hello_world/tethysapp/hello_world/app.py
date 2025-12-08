from tethys_sdk.base import TethysAppBase, url_map_maker

class App(TethysAppBase):
    name = 'Hello World'
    package = 'hello_world'
    index = 'home'  # This must match the UrlMap name
    root_url = 'hello-world'
    icon = f'{package}/images/icon.gif'

    def url_maps(self):
        UrlMap = url_map_maker(self.root_url)
        url_maps = (
            UrlMap(
                name='home',  # Must match index
                url='',
                controller='hello_world.controllers.home_page'
            ),
            UrlMap(
                name='map',
                url='map',
                controller='hello_world.controllers.map_page'
            ),
        )
        return url_maps