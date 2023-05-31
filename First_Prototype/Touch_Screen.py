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
from kivy import Config
import pigpio



Config.set('graphics', 'multisamples', '0')
Window.fullscreen = 'auto'

class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        
        super(MDScreen, self).__init__(**kwargs)
        self.nav = Menu()
        self.add_widget(self.nav)

class Menu(MDBottomNavigation):
    
    def __init__(self, **kwargs):
        
        self.pi = pigpio.pi()
        self.I2C_SLAVE_ADDRESS = 105  # Change this to the desired slave address

        self.pi.set_pull_up_down(2, pigpio.PUD_UP)
        self.pi.set_pull_up_down(3, pigpio.PUD_UP)

        self.I2C_CB_Fun = self.pi.event_callback(pigpio.EVENT_BSC, self.i2c_callback)
        self.pi.bsc_i2c(self.I2C_SLAVE_ADDRESS) # Configure BSC as I2C slave

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

        self.Settings.Layout.CityLayout.City.text = data['City_Code'] 
        self.Settings.Layout.CountryLayout.Country.text = data['Country_Code']
        self.Settings.Layout.UnitsLayout.Units.text = data['Units']

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

        data['City_Code'] = self.Settings.Layout.CityLayout.City.text
        data['Country_Code'] = self.Settings.Layout.CountryLayout.Country.text
        data['Units'] = self.Settings.Layout.UnitsLayout.Units.text

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

    def i2c_callback(self, id, tick):

        # Process data to send

        self.whiteValueForRed = self.Leds.Layout.Setting.Layout.Color.icon_color[0] * 255.0 / 255.0
        self.whiteValueForGreen = self.Leds.Layout.Setting.Layout.Color.icon_color[1] * 255.0 / 173.0
        self.whiteValueForBlue = self.Leds.Layout.Setting.Layout.Color.icon_color[2] * 255.0 / 94.0

        self.minWhiteValue = min(self.whiteValueForRed, self.whiteValueForGreen, self.whiteValueForBlue)

        self.Wo = self.minWhiteValue if self.minWhiteValue <= 255 else 255

        self.Ro = int(self.Leds.Layout.Setting.Layout.Color.icon_color[0] - self.minWhiteValue * 255 / 255)
        self.Go = int(self.Leds.Layout.Setting.Layout.Color.icon_color[1] - self.minWhiteValue * 173 / 255)
        self.Bo = int(self.Leds.Layout.Setting.Layout.Color.icon_color[2]  - self.minWhiteValue * 94 / 255)

        if self.Leds.Layout.Setting.Layout.Color.icon == "lightbulb-outline":
            self.Wo = 0
            self.Ro = 0
            self.Go = 0
            self.Bo = 0

        # Send a response
        response_data = [0, 
                         self.Bo, 
                         self.Wo, 
                         self.Ro, 
                         self.Go, 
                         self.Media.Layout.Volume.Slider.value, 
                         self.Source.MainLayout.Bass.Slider.value, 
                         self.Source.MainLayout.Mid.Slider.value, 
                         self.Source.MainLayout.Treble.Slider.value]  # Change this with your response data
        
        s, b, d = self.pi.bsc_i2c(self.I2C_SLAVE_ADDRESS)
        if b:

            print("sent={} FR={} received={} [{}]".
                   format(s>>16, s&0xfff,b,d))

            self.pi.bsc_i2c(self.I2C_SLAVE_ADDRESS, response_data)

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
                    on_press=self.closeApp
                ),
            ],
        )
        self.dialog.open()

    def closeDialog(self, xd):
        self.dialog.dismiss()

    def closeApp(self, xd):
        self.parent.I2C_CB_Fun.cancel()
        self.parent.pi.bsc_i2c(0)
        self.parent.pi.stop()
        lambda x: MDApp.get_running_app().stop()



class Example(MDApp):

    def build(self):
        Debug.enableConsole = True
        os.chdir(pathlib.Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainScreen()

if __name__ == '__main__':
    Example().run()