from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.behaviors import FocusBehavior
from kivymd.uix.card import MDCard


KV = '''
MDScreen:
	fd: field
	canvas:
		Color:
			rgba: 0,0,0,1
		Line:
			rounded_rectangle:0.45*root.center_x,root.center_y-dp(15),0.56*root.width,50,10
			width: 0.5
	MDTextField:
		id: field
		size_hint_x: 0.55
		center_y: root.center_y
		line_color_normal: 0,0,0,1
		line_color_focus: 0,0,0,1
		line_anim: False
		x: 0.46*root.center_x
		font_size: "15sp"
'''


class CustomField(MDCard):
    pass


class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Builder.load_string(KV)


TestApp().run()
