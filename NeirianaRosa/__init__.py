from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from NeirianaRosa.uix.object.macro.manager import Manager

class NeirianaRosaApp(MDApp):
    def __init__(self):
        super().__init__()
        self.load_kvs()
        
        
    def build(self):
        self.manager = Manager()
        return self.manager

    def goto(self,name):
        self.manager.transition.direction = 'left'
        self.manager.current = name
    
    def check_back(self):
        mapa = {'Story':'Generate Story','Generate Story':'Menu','Tabua':'Menu'}
        if self.manager.current == 'Menu':
            return False
        else:
            self.manager.transition.direction = 'right'
            self.manager.current = mapa[self.manager.current]
            return True
        

        

    def _on_keyboard_settings(self, window, key, *args):
        if key == 27:
            return self.check_back()
        return True

    def load_kvs(self):
        self.load_kv('./NeirianaRosa/uix/kv/screen/menu.kv')
        self.load_kv('./NeirianaRosa/uix/kv/screen/story.kv')
        self.load_kv('./NeirianaRosa/uix/kv/screen/generate_story.kv')
        self.load_kv('./NeirianaRosa/uix/kv/screen/tabua.kv')
        self.load_kv('./NeirianaRosa/uix/kv/macro/manager.kv')
        self.load_kv('./NeirianaRosa/uix/kv/widget/star.kv')
        self.load_kv('./NeirianaRosa/uix/kv/widget/row.kv')

