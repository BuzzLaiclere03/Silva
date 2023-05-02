import pathlib
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import os
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from Media import MediaMenu
    
class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        
        super(MDScreen, self).__init__(**kwargs)
        self.nav = Menu()
        self.add_widget(self.nav)

class Menu(MDBottomNavigation):
    
    def __init__(self, **kwargs):
        
        super(Menu, self).__init__(**kwargs)
        Debug.Start("Menu -> __init__")
        Debug.Log("self.media")
        self.media = MediaMenu()
        Debug.Log("adding media")
        self.add_widget(self.media)
        Debug.Log("self.source")
        self.source = SourceMenu()
        Debug.Log("adding source")
        self.add_widget(self.source)
        Debug.Log("self.settings")
        self.settings = SettingsMenu()
        Debug.Log("Adding settings")
        self.add_widget(self.settings)
        Debug.End()

class SourceMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(SourceMenu, self).__init__(**kwargs)
        self.name = "SourceMenu"
        self.text = "Source"
        self.icon = "bluetooth"
        self.label = MDLabel(text='Source', halign='center')
        self.add_widget(self.label)

class SettingsMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(SettingsMenu, self).__init__(**kwargs)
        self.name = "SettingsMenu"
        self.text = "Settings"
        self.icon = "cog"
        self.label = MDLabel(text='Settings', halign='center')
        self.add_widget(self.label)

class Example(MDApp):

    def build(self):
        Debug.enableConsole = True
        os.chdir(pathlib.Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainScreen()

if __name__ == '__main__':
    Example().run()