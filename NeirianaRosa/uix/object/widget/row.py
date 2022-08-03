from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty

class Row(MDBoxLayout):
    text_1 = StringProperty()
    text_2 = StringProperty()
    def __init__(self,text_1,text_2):
        super().__init__()
        self.text_1 = text_1
        self.text_2 = text_2