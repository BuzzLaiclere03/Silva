import pathlib
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import os
import json
from kivy.clock import Clock
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from Media import MediaMenu
from Source import SourceMenu
from Settings import SettingsMenu
from Leds import LedsMenu

class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        
        super(MDScreen, self).__init__(**kwargs)
        self.nav = Menu()
        self.add_widget(self.nav)

class Menu(MDBottomNavigation):
    
    def __init__(self, **kwargs):
        
        super(Menu, self).__init__(**kwargs)
        Debug.Start("Menu -> __init__")
        Clock.schedule_interval(self.JSONupdate, 0.5)
        Debug.Log("self.Media")
        self.Media = MediaMenu()
        Debug.Log("adding Media")
        self.add_widget(self.Media)
        Debug.Log("self.Leds")
        self.Leds = LedsMenu()
        Debug.Log("adding Leds")
        self.add_widget(self.Leds)
        Debug.Log("self.Source")
        self.Source = SourceMenu()
        Debug.Log("adding Source")
        self.add_widget(self.Source)
        Debug.Log("self.Settings")
        self.Settings = SettingsMenu()
        Debug.Log("Adding Settings")
        self.add_widget(self.Settings)
        Debug.End()

    def JSONupdate(self, dt):

        # Open the file for reading
        with open('Data_TS_W.json', 'r') as f:
            data = json.load(f)

        data['Music_State'] = self.Media.Layout.Control.Play.icon
        data['Music_Volume'] = self.Media.Layout.Volume.Slider.value
        data['Music_Time'] = self.Media.Layout.Time.Slider.value
        data['Music_Next'] = self.Media.Layout.Control.Next.NextPressed
        data['Music_Back'] = self.Media.Layout.Control.Back.BackPressed
        data['Zip_Code'] = self.Settings.Layout.Zip.text
        data['Country_Code'] = self.Settings.Layout.Country.text
        data['Units'] = self.Settings.Layout.Units.text
        data['Source'] = self.Source.MainLayout.Selected
        data['NewSource'] = self.Source.MainLayout.NewSource

        # Open the file for writing
        with open('Data_TS_W.json', 'w') as f:
            json.dump(data, f)

        # Close the file
        f.close()


class Example(MDApp):

    def build(self):
        Debug.enableConsole = True
        os.chdir(pathlib.Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainScreen()

if __name__ == '__main__':
    Example().run()