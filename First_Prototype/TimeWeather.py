from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from datetime import datetime
from kivy.clock import Clock
import requests
import string

class Time_Date(MDStackLayout):

    def __init__(self, **kwargs):
        
        super(Time_Date, self).__init__(**kwargs)
        self.name = "Time_Date"
        self.orientation = 'tb-rl'
        self.size_hint = (1, 1)
        self.padding = '40dp'
        self.spacing = '50dp'
        self.Time = TimeLabel()
        self.add_widget(self.Time)
        self.Date = DateLabel()
        self.add_widget(self.Date)
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        self.now = datetime.now()
        self.Time.text = self.now.strftime('%H:%M:%S')

        if self.Time.text == "00:00:00":
            self.Date.text = self.now.strftime("%A %d. %B %Y")

class TimeLabel(MDLabel):

    def __init__(self, **kwargs):
        
        super(TimeLabel, self).__init__(**kwargs)
        self.name = "Time"
        self.font_style = 'H1'
        self.font_size = '150dp'
        self.now = datetime.now()
        self.text = self.now.strftime('%H:%M:%S')
        self.size_hint_y = 0.3
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.halign = 'right'

class DateLabel(MDLabel):

    def __init__(self, **kwargs):
        
        super(DateLabel, self).__init__(**kwargs)
        self.name = "Date"
        self.font_style = 'H2'
        self.today = datetime.today()
        self.text = self.today.strftime("%A %d. %B %Y")
        self.size_hint_y = 0.3
        self.halign = 'right'

class WeatherMainLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(WeatherMainLayout, self).__init__(**kwargs)
        self.name = "WeatherMainLayout"
        self.orientation = 'horizontal'
        self.settings = {
            'api_key':'11aa74498d969db8b9703c0357d6671c',
            'city':'Quebec',
            'country_code':'ca',
            'temp_unit':'metric'} #unit can be metric, imperial, or kelvin

        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={0},{1}&appid={2}&units={3}"
        self.final_url = self.BASE_URL.format(self.settings["city"],self.settings["country_code"],self.settings["api_key"],self.settings["temp_unit"])
        self.weather_data = requests.get(self.final_url).json()
        print(self.weather_data)
        self.padding = "20dp"
        self.Icon = WeatherIcon()
        self.add_widget(self.Icon)
        self.InfoLayout = WeatherInfoLayout()
        self.add_widget(self.InfoLayout)
        
        #self.size_hint_y = 0.25
        Clock.schedule_interval(self.update_weather, 300)
        self.update_weather()

    def update_weather(self, *args):
        # Called once every 5 minutes using the kivy.clock module
        self.Weather = self.weather_data['weather'][0]['icon']

        if self.Weather == "01d":
            self.Icon.icon = "weather-sunny"
        elif self.Weather == "01n":
            self.Icon.icon = "weather-night"
        elif self.Weather == "02d":
            self.Icon.icon = "weather-partly-cloudy"
        elif self.Weather == "02n":
            self.Icon.icon = "weather-night-partly-cloudy"
        elif self.Weather == "03d":
            self.Icon.icon = "weather-cloud"
        elif self.Weather == "03n":
            self.Icon.icon = "weather-cloud"
        elif self.Weather == "04d":
            self.Icon.icon = "cloud"
        elif self.Weather == "04n":
            self.Icon.icon = "cloud"
        elif self.Weather == "09d":
            self.Icon.icon = "weather-pouring"
        elif self.Weather == "09n":
            self.Icon.icon = "weather-pouring"
        elif self.Weather == "10d":
            self.Icon.icon = "weather-partly-rainy"
        elif self.Weather == "10n":
            self.Icon.icon = "weather-rainy"
        elif self.Weather == "11d":
            self.Icon.icon = "weather-lightning"
        elif self.Weather == "11n":
            self.Icon.icon = "weather-lightning"
        elif self.Weather == "13d":
            self.Icon.icon = "weather-partly-snowy"
        elif self.Weather == "13n":
            self.Icon.icon = "weather-snowy"
        elif self.Weather == "50d":
            self.Icon.icon = "weather-hazy"
        elif self.Weather == "50n":
            self.Icon.icon = "weather-fog"

        self.InfoLayout.Desc.Text.text = string.capwords(self.weather_data['weather'][0]['description'])
        self.InfoLayout.Temp.Num.text = str(self.weather_data['main']['temp']) + " (" + str(self.weather_data['main']['feels_like']) + ") °C"
        self.InfoLayout.Hum.Percent.text = str(self.weather_data['main']['humidity']) + "%"
 
class WeatherIcon(MDIcon):

    def __init__(self, **kwargs):
        
        super(WeatherIcon, self).__init__(**kwargs)
        self.name = "WeatherIcon"
        #self.size_hint = (1, 1)
        self.icon = "blank"
        self.font_size = "150dp"
        self.pos_hint = {"center_x":0.8, "center_y":0.5}

class WeatherInfoLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(WeatherInfoLayout, self).__init__(**kwargs)
        self.name = "WeatherInfoLayout"
        self.orientation = 'vertical'
        self.padding = (0, "100dp")
        self.Desc = WeatherDesc()
        self.add_widget(self.Desc)
        self.Temp = WeatherTemp()
        self.add_widget(self.Temp)
        self.Hum = WeatherHum()
        self.add_widget(self.Hum)

class WeatherDesc(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(WeatherDesc, self).__init__(**kwargs)
        self.name = "WeatherDesc"
        self.orientation = 'horizontal'
        self.Text = DescText()
        self.add_widget(self.Text)
        self.Icon = DescIcon()
        self.add_widget(self.Icon)

class DescText(MDLabel):

    def __init__(self, **kwargs):
        
        super(DescText, self).__init__(**kwargs)
        self.name = "DescText"
        self.font_style = 'H4'
        self.halign = 'center'
        self.size_hint_x = 0.7

class DescIcon(MDIcon):

    def __init__(self, **kwargs):
        
        super(DescIcon, self).__init__(**kwargs)
        self.name = "DescIcon"
        self.icon = "menu"
        self.font_size = "50dp"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

class WeatherTemp(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(WeatherTemp, self).__init__(**kwargs)
        self.name = "WeatherTemp"
        self.orientation = 'horizontal'
        self.Num = TempNum()
        self.add_widget(self.Num)
        self.Icon = TempIcon()
        self.add_widget(self.Icon)

class TempIcon(MDIcon):

    def __init__(self, **kwargs):
        
        super(TempIcon, self).__init__(**kwargs)
        self.name = "HumIcon"
        self.icon = "thermometer"
        self.font_size = "50dp"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

class TempNum(MDLabel):

    def __init__(self, **kwargs):
        
        super(TempNum, self).__init__(**kwargs)
        self.name = "WeatherTemp"
        self.font_style = 'H4'
        self.halign = 'center'
        self.size_hint_x = 0.7

class WeatherHum(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(WeatherHum, self).__init__(**kwargs)
        self.name = "WeatherHum"
        self.orientation = 'horizontal'
        self.Percent = HumPercent()
        self.add_widget(self.Percent)
        self.Icon = HumIcon()
        self.add_widget(self.Icon)

class HumIcon(MDIcon):

    def __init__(self, **kwargs):
        
        super(HumIcon, self).__init__(**kwargs)
        self.name = "HumIcon"
        self.icon = "water-percent"
        self.font_size = "50dp"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

class HumPercent(MDLabel):

    def __init__(self, **kwargs):
        
        super(HumPercent, self).__init__(**kwargs)
        self.name = "HumPercent"
        self.font_style = 'H4'
        self.halign = 'center'
        self.size_hint_x = 0.7








        




class MediaTimeLeft(MDLabel):

    def __init__(self, **kwargs):
        
        super(MediaTimeLeft, self).__init__(**kwargs)
        self.name = "MediaTimeLeft"
        self.text = "-0:00"
        self.font_style = 'H4'
        self.size_hint_x = 0.25
        self.halign = 'center'

class MediaPlayButton(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaPlayButton, self).__init__(**kwargs)
        self.name = "MediaPlayButton"
        self.size_hint = (0.3,0.3) 
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.on_press = self.Pressed
        self.icon = "play"
        self.icon_size = "75dp"

    def Pressed(self):

        Debug.Start("MediaPlayButton -> Pressed")

        if self.icon == "pause":
            Debug.Log("Was pause, is now play")
            self.icon = "play"
        elif self.icon == "play":
            Debug.Log("Was play, is now pause")
            self.icon = "pause"

        Debug.End()

class MediaNextButton(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaNextButton, self).__init__(**kwargs)
        self.name = "MediaNextButton"
        self.icon = "skip-next"
        self.icon_size = "75dp"
        self.size_hint = (0.3,0.3) 
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.NextPressed = False
        self.on_press = self.Pressed

    def Pressed(self):

        Debug.Start("MediaNextButton -> Pressed")

        self.NextPressed = True

        Debug.End()

class MediaBackButton(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaBackButton, self).__init__(**kwargs)
        self.name = "MediaBackButton"
        self.icon = "skip-previous"
        self.icon_size = "75dp"
        self.size_hint = (0.3,0.3) 
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.BackPressed = False
        self.on_press = self.Pressed

    def Pressed(self):

        Debug.Start("MediaBackButton -> Pressed")

        self.BackPressed = True

        Debug.End()

class MediaVolumeLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MediaVolumeLayout, self).__init__(**kwargs)
        self.name = "MediaControlLayout"
        self.orientation = 'horizontal'
        self.size_hint_y = 0.25
        self.IconDown = MediaVolumeDownIcon()
        self.add_widget(self.IconDown)
        self.Slider = MediaVolumeSlider()
        self.add_widget(self.Slider)
        self.IconUp = MediaVolumeUpIcon()
        self.add_widget(self.IconUp)

class MediaVolumeSlider(MDSlider):

    def __init__(self, **kwargs):
        
        super(MediaVolumeSlider, self).__init__(**kwargs)
        self.name = "MediaVolumeSlider"
        self.range = (0, 100)
        self.orientation = 'horizontal'
        self.step = 5
        self.value = 25
        self.hint = True
        self.size_hint_x = 0.5
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

class MediaVolumeUpIcon(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaVolumeUpIcon, self).__init__(**kwargs)
        self.name = "MediaVolumeUpIcon"
        self.icon = "volume-high"
        self.icon_size = "50dp"
        self.size_hint_x = 0.25
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

class MediaVolumeDownIcon(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaVolumeDownIcon, self).__init__(**kwargs)
        self.name = "MediaVolumeDownIcon"
        self.icon = "volume-medium"
        self.icon_size = "50dp"
        self.size_hint_x = 0.25
        self.pos_hint = {"center_x":0.5, "center_y":0.5}