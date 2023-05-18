import pathlib
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
import os
import json
from kivy.clock import Clock
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from TimeWeather import Time_Date, WeatherMainLayout
from kivy.core.window import Window
#from kivymd.uix.pickers import MDDatePicker
from Calendar import MDDatePicker
    
Window.left = -2000
Window.fullscreen = 'auto'

class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        
        super(MDScreen, self).__init__(**kwargs)
        self.Card = MainCard()
        self.add_widget(self.Card)

class MainCard(MDCard):

    def __init__(self, **kwargs):
        super(MainCard, self).__init__(**kwargs)
        self.bg_color = (0, 0, 0)
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.orientation ='vertical'
        self.Time = Time_Date()
        self.Time.size_hint = (1, 0.25)
        self.add_widget(self.Time)
        self.Layout = MainLayout()
        self.add_widget(self.Layout)

class MainLayout(MDGridLayout):
    
    def __init__(self, **kwargs):
        
        super(MainLayout, self).__init__(**kwargs)
        Debug.Start("MainLayout -> __init__")
        #Clock.schedule_interval(self.JSONupdate, 0.5)
        self.cols = 2
        self.rows = 3
        self.Weather = WeatherMainLayout()
        self.add_widget(self.Weather)

        self.date_dialog = MDDatePicker(year=1983, month=4, day=12)
        self.add_widget(self.date_dialog)
        self.Time3 = MDBoxLayout()
        self.add_widget(self.Time3)
        self.Time4 = MDBoxLayout()
        self.add_widget(self.Time4)
        self.Time5 = MDBoxLayout()
        self.add_widget(self.Time5)
        self.Time6 = MDBoxLayout()
        self.add_widget(self.Time6)
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


class Prototype(MDApp):

    def build(self):
        Debug.enableConsole = True
        os.chdir(pathlib.Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return MainScreen()

if __name__ == '__main__':
    Prototype().run()
