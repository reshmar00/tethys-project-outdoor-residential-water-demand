from tethys_sdk.base import TethysAppBase, url_map_maker

class HelloWorld(TethysAppBase):
    name = 'Hello World'
    package = 'hello_world'
    index = 'home'          # Home page is the index
    root_url = 'hello-world'
    icon = f'{package}/images/icon.gif'

    def url_maps(self):
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='',
                controller='hello_world.controllers.home_page'
            ),
        )
        return url_maps