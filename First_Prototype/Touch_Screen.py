import pathlib
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import os
import json
    
class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        
        super(MDScreen, self).__init__(**kwargs)
        self.nav = Menu()
        self.add_widget(self.nav)

class Menu(MDBottomNavigation):
    
    def __init__(self, **kwargs):
        
        super(MDBottomNavigation, self).__init__(**kwargs)
        self.media = MediaMenu()
        self.add_widget(self.media)
        self.source = SourceMenu()
        self.add_widget(self.source)
        self.settings = SettingsMenu()
        self.add_widget(self.settings)

class MediaMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MDBottomNavigationItem, self).__init__(**kwargs)
        self.name = "MediaMenu"
        self.text = "Media"
        self.icon = "music-box"
        self.label = MDLabel(text='Media', halign='center')
        self.add_widget(self.label)

class SourceMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MDBottomNavigationItem, self).__init__(**kwargs)
        self.name = "SourceMenu"
        self.text = "Source"
        self.icon = "bluetooth-settings"
        self.label = MDLabel(text='Source', halign='center')
        self.add_widget(self.label)

class SettingsMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MDBottomNavigationItem, self).__init__(**kwargs)
        self.name = "SettingsMenu"
        self.text = "Settings"
        self.icon = "cog"
        self.label = MDLabel(text='Settings', halign='center')
        self.add_widget(self.label)

class Example(MDApp):

    def build(self):
        os.chdir(pathlib.Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainScreen()

if __name__ == '__main__':
    Example().run()