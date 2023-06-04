from pathlib import Path
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
        #Debug.Log("self.QuitButton")
        #self.QuitButton = Quit()
        #Debug.Log("Adding QuitButton")
        #self.add_widget(self.QuitButton)
        self.updateInfoFromJSON()
        Clock.schedule_interval(self.JSONupdate, 1)

        self.pi = pigpio.pi()
        #self.pi.bsc_i2c(0) # Disable BSC peripheral
        self.I2C_SLAVE_ADDRESS = 0x69  # Change this to the desired slave address

        #self.pi.set_pull_up_down(2, pigpio.PUD_UP)
        #self.pi.set_pull_up_down(3, pigpio.PUD_UP)

        self.handle = self.pi.i2c_open(1, self.I2C_SLAVE_ADDRESS)
        Clock.schedule_interval(self.i2c_callback, 0.1)
        #self.pi.bsc_i2c(self.I2C_SLAVE_ADDRESS) # Configure BSC as I2C slave
        #self.i2c_callback(3, 4)

        Debug.End()

    def updateInfoFromJSON(self):

        # Open the file for reading
        with open('Data_TS_W.json', 'r') as f:
            data = json.load(f)

        self.Settings.Layout.CityLayout.City.text = data['City_Code'] 
        self.Settings.Layout.CountryLayout.Country.text = data['Country_Code']
        self.Settings.Layout.UnitsLayout.Units.text = data['Units']

        self.Leds.Layout.Selection.Color1.icon_color = data['ColorPreset1']
        self.Leds.Layout.Selection.Color2.icon_color = data['ColorPreset2']
        self.Leds.Layout.Selection.Color3.icon_color = data['ColorPreset3']
        self.Leds.Layout.Selection.Color4.icon_color = data['ColorPreset4']

        self.Media.Layout.Volume.Slider.value = data['Volume']
        self.Source.MainLayout.Bass.Slider.value = data['Bass']  
        self.Source.MainLayout.Mid.Slider.value = data['Mid']   
        self.Source.MainLayout.Treble.Slider.value = data['Treble']

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

        data['ColorPreset1'] = self.Leds.Layout.Selection.Color1.icon_color
        data['ColorPreset2'] = self.Leds.Layout.Selection.Color2.icon_color
        data['ColorPreset3'] = self.Leds.Layout.Selection.Color3.icon_color
        data['ColorPreset4'] = self.Leds.Layout.Selection.Color4.icon_color

        data['Title'] = self.Media.Layout.title
        data['Artist'] = self.Media.Layout.artist
        data['Album'] = self.Media.Layout.album

        data['Volume'] = self.Media.Layout.Volume.Slider.value
        data['Bass'] = self.Source.MainLayout.Bass.Slider.value
        data['Mid'] = self.Source.MainLayout.Mid.Slider.value
        data['Treble'] = self.Source.MainLayout.Treble.Slider.value

        # Open the file for writing
        with open('Data_TS_W.json', 'w') as f:
            json.dump(data, f)

        # Close the file
        f.close()

    def i2c_callback(self, dt):
        
        kWhiteRedChannel = 255
        kWhiteGreenChannel = 177
        kWhiteBlueChannel = 101

        # Process data to send

        r = self.Leds.Layout.Setting.Layout.Color.icon_color[0]
        g = self.Leds.Layout.Setting.Layout.Color.icon_color[1]
        b = self.Leds.Layout.Setting.Layout.Color.icon_color[2] 

        white_value_for_red = r * 255.0 / kWhiteRedChannel
        white_value_for_green = g * 255.0 / kWhiteGreenChannel
        white_value_for_blue = b * 255.0 / kWhiteBlueChannel

        min_white_value = min(white_value_for_red, min(white_value_for_green, white_value_for_blue))
        self.Wo = min_white_value if min_white_value <= 255 else 255
        self.Wo = int(self.Wo * 255)

        self.Ro = r - min_white_value * kWhiteRedChannel // 255
        self.Ro = int(self.Ro * 255)
        self.Go = g - min_white_value * kWhiteGreenChannel // 255
        self.Go = int(self.Go * 255)
        self.Bo = b - min_white_value * kWhiteBlueChannel // 255
        self.Bo = int(self.Bo * 255)
    

        if self.Leds.Layout.Setting.Layout.Color.icon == "lightbulb-outline":
            self.Wo = 0
            self.Ro = 0
            self.Go = 0
            self.Bo = 0

        checksum = 0
        # Send a response
        response_data = [0x24, 
                         self.Bo, 
                         self.Wo, 
                         self.Ro, 
                         self.Go, 
                         self.Media.Layout.Volume.Slider.value, 
                         self.Source.MainLayout.Bass.Slider.value,
                         self.Source.MainLayout.Mid.Slider.value, 
                         self.Source.MainLayout.Treble.Slider.value,
                         checksum]  # Change this with your response data

        for x in range(9):
            if x != 0:
                if response_data[x] == 0x24:
                    response_data[x] += 1

        checksum = 0x24 + self.Bo + self.Wo + self.Ro + self.Go + self.Media.Layout.Volume.Slider.value + self.Source.MainLayout.Bass.Slider.value + self.Source.MainLayout.Mid.Slider.value + self.Source.MainLayout.Treble.Slider.value
        checksum %= 255

        if checksum == 0x24:
            checksum += 1
        
        response_data[9] = checksum
        
        print(response_data)
        
        #s, b, d = self.pi.bsc_i2c(self.I2C_SLAVE_ADDRESS)

        #self.pi.bsc_i2c(self.I2C_SLAVE_ADDRESS, response_data)
        self.pi.i2c_write_i2c_block_data(self.handle, response_data[0], response_data[1:])

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
        #self.I2C_CB_Fun.cancel()
        #self.parent.pi.bsc_i2c(0)
        #self.parent.pi.stop()
        lambda x: MDApp.get_running_app().stop()



class Example(MDApp):

    def build(self):
        Debug.enableConsole = True
        os.chdir(Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainScreen()

if __name__ == '__main__':
    Example().run()