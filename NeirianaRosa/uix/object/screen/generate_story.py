from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class GenerateStory(MDScreen):
    def to_screen(self,text):
        MDApp.get_running_app().manager.current = 'Story'
        MDApp.get_running_app().manager.ids.story.text = text

        
