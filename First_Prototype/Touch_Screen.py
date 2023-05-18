import pathlib
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import os
import json
from kivy.clock import Clock
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from Media import MediaMenu
from Source import SourceMenu
from Settings import SettingsMenu
from Leds import LedsMenu
from kivy.core.window import Window

Window.fullscreen = 'auto'

class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        
        super(MDScreen, self).__init__(**kwargs)
        self.nav = Menu()
        self.add_widget(self.nav)

class Menu(MDBottomNavigation):
    
    def __init__(self, **kwargs):
        
        super(Menu, self).__init__(**kwargs)
        Debug.Start("Menu -> __init__")
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
        Debug.Log("self.QuitButton")
        self.QuitButton = Quit()
        Debug.Log("Adding QuitButton")
        self.add_widget(self.QuitButton)
        self.updateInfoFromJSON()
        Clock.schedule_interval(self.JSONupdate, 0.5)
        Debug.End()

    def updateInfoFromJSON(self):

        # Open the file for reading
        with open('Data_TS_W.json', 'r') as f:
            data = json.load(f)

        self.Media.Layout.Volume.Slider.value = data['Music_Volume']
        self.Settings.Layout.CityLayout.City.text = data['City_Code'] 
        self.Settings.Layout.CountryLayout.Country.text = data['Country_Code']
        self.Settings.Layout.UnitsLayout.Units.text = data['Units']
        self.Source.MainLayout.Selected = data['Source'] 
        self.Leds.Layout.Setting.Layout.Color.icon_color = data['SelectedColor']
        self.Leds.Layout.Selection.Color1.icon_color = data['ColorPreset1']
        self.Leds.Layout.Selection.Color2.icon_color = data['ColorPreset2']
        self.Leds.Layout.Selection.Color3.icon_color = data['ColorPreset3']
        self.Leds.Layout.Selection.Color4.icon_color = data['ColorPreset4']

        # Open the file for writing
        with open('Data_TS_W.json', 'w') as f:
            json.dump(data, f)

        # Close the file
        f.close()

    def JSONupdate(self, dt):

        # Open the file for reading
        with open('Data_TS_W.json', 'r') as f:
            data = json.load(f)

        data['Music_State'] = self.Media.Layout.Control.Play.icon
        data['Music_Volume'] = self.Media.Layout.Volume.Slider.value
        data['Music_Time'] = self.Media.Layout.Time.Slider.value
        data['Music_Next'] = self.Media.Layout.Control.Next.NextPressed
        data['Music_Back'] = self.Media.Layout.Control.Back.BackPressed
        data['City_Code'] = self.Settings.Layout.CityLayout.City.text
        data['Country_Code'] = self.Settings.Layout.CountryLayout.Country.text
        data['Units'] = self.Settings.Layout.UnitsLayout.Units.text
        data['NewSource'] = self.Source.MainLayout.NewSource
        if self.Leds.Layout.Setting.Layout.Color.icon == "lightbulb":
            data['LedsOn'] = 1
        elif self.Leds.Layout.Setting.Layout.Color.icon == "lightbulb-outline":
            data['LedsOn'] = 0
        data['SelectedColor'] = self.Leds.Layout.Setting.Layout.Color.icon_color
        data['ColorPreset1'] = self.Leds.Layout.Selection.Color1.icon_color
        data['ColorPreset2'] = self.Leds.Layout.Selection.Color2.icon_color
        data['ColorPreset3'] = self.Leds.Layout.Selection.Color3.icon_color
        data['ColorPreset4'] = self.Leds.Layout.Selection.Color4.icon_color

        # Open the file for writing
        with open('Data_TS_W.json', 'w') as f:
            json.dump(data, f)

        # Close the file
        f.close()

class Quit(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(Quit, self).__init__(**kwargs)
        self.name = "Quit"
        self.text = "Quit"
        self.icon = "exit-to-app"
        self.on_tab_press = self.show_alert_dialog

    def show_alert_dialog(self):
        #if not self.dialog:
        self.dialog = MDDialog(
            text="Do you really want to quit?",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=self.closeDialog
                ),
                MDFlatButton(
                    text="QUIT",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=lambda x: MDApp.get_running_app().stop()
                ),
            ],
        )
        self.dialog.open()

    def closeDialog(self, xd):
        self.dialog.dismiss()


class Example(MDApp):

    def build(self):
        Debug.enableConsole = True
        os.chdir(pathlib.Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainScreen()

if __name__ == '__main__':
    Example().run()