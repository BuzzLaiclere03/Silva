import pathlib
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import os
import json
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
    
class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        
        super(MDScreen, self).__init__(**kwargs)
        self.nav = Menu()
        self.add_widget(self.nav)

class Menu(MDBottomNavigation):
    
    def __init__(self, **kwargs):
        
        super(MDBottomNavigation, self).__init__(**kwargs)
        Debug.Start("Menu -> __init__")
        Debug.Log("self.media")
        media = MediaMenu()
        Debug.Log("adding media")
        self.add_widget(media)
        Debug.Log("self.source")
        self.source = SourceMenu()
        Debug.Log("adding source")
        self.add_widget(self.source)
        Debug.Log("self.settings")
        self.settings = SettingsMenu()
        Debug.Log("Adding settings")
        self.add_widget(self.settings)
        Debug.End()

class MediaMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MDBottomNavigationItem, self).__init__(**kwargs)
        self.name = "MediaMenu"
        self.text = "Media"
        self.icon = "music-box"
        self.label = MDLabel(text='Media', halign='center')
        self.add_widget(self.label)

    def on_switch_tabs(self, **kwargs):
        super(MDBottomNavigationItem, self).__init__(**kwargs)

class SourceMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MDBottomNavigationItem, self).__init__(**kwargs)
        self.name = "SourceMenu"
        self.text = "Source"
        self.icon = "bluetooth-settings"
        self.label = MDLabel(text='Source', halign='center')
        self.add_widget(self.label)

    def on_switch_tabs(self, **kwargs):
        super(MDBottomNavigationItem, self).__init__(**kwargs)

class SettingsMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MDBottomNavigationItem, self).__init__(**kwargs)
        self.name = "SettingsMenu"
        self.text = "Settings"
        self.icon = "cog"
        self.label = MDLabel(text='Settings', halign='center')
        self.add_widget(self.label)

    def on_switch_tabs(self, **kwargs):
        super(MDBottomNavigationItem, self).__init__(**kwargs)

class Example(MDApp):

    def build(self):
        Debug.enableConsole = True
        os.chdir(pathlib.Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainScreen()

if __name__ == '__main__':
    Example().run()