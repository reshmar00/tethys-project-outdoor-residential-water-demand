from tethys_sdk.base import TethysAppBase, url_map_maker

class App(TethysAppBase):
    name = 'Hello World'
    package = 'hello_world'
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'hello-world'
    color = '#00FFFF'
    description = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        UrlMap = url_map_maker(self.root_url)
        url_maps = (
            UrlMap(
                name='home',
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