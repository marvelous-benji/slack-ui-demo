from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
#from kivy.utils import get_color_from_hex



class Home(MDFloatLayout):
    pass


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return Home()


if __name__ == '__main__':
    DemoApp().run()