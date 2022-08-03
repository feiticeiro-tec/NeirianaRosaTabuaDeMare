from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.utils.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivy.properties import StringProperty,ListProperty

class Star(MDBoxLayout):
    image = StringProperty()
    text = StringProperty()
    def __init__(self,image,text,height):
        super().__init__()
        self.image = image
        self.text = text
        self.height = height


class Stars(MDBoxLayout):
    def __init__(self,image=None, nasce=None,poe=None):
        super().__init__()
        self.adaptive_height = True
        if image == 'sol':
            if nasce:
                self.add_widget(Star('./NeirianaRosa/img/sol.png',nasce,dp(80)))
            if poe:
                self.add_widget(Star('./NeirianaRosa/img/sol_poe.png',poe,dp(80)))
        elif image == 'lua':
            if nasce:
                self.add_widget(Star('./NeirianaRosa/img/lua.png',nasce,dp(80)))
            if poe:
                self.add_widget(Star('./NeirianaRosa/img/lua_poe.png',poe,dp(80)))
        