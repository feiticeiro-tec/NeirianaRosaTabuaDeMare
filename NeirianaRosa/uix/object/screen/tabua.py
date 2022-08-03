from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from NeirianaRosa.get_table import getNow
from NeirianaRosa.uix.object.widget.star import Star,Stars
from NeirianaRosa.uix.object.widget.row import Row
from kivy.properties import StringProperty

from pprint import pprint

class Tabua(MDScreen):
    data = StringProperty()
    def on_enter(self):
        data = getNow()
        pprint(data)
        self.data = f'{data["day"]:0>2}/{data["mon"]:0>2}'
        self.ids.article.clear_widgets()
        self.ids.article.add_widget(Row('Horas','Altura(m)'))
        for item in data['article']:
            self.ids.article.add_widget(Row(item['Timer'],item['Nivel']))
        
        self.ids.stars.clear_widgets()
        self.ids.stars.add_widget(Stars('sol',data['stars'].get('sol nasce'),data['stars'].get('sol se põe')))
        self.ids.stars.add_widget(Stars('lua',data['stars'].get('lua nasce'),data['stars'].get('lua se põe')))
        
        return super().on_enter()