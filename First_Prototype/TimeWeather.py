from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from datetime import datetime
from kivy.clock import Clock

class Time_Date(MDStackLayout):

    def __init__(self, **kwargs):
        
        super(Time_Date, self).__init__(**kwargs)
        self.name = "Time_Date"
        self.orientation = 'tb-rl'
        #self.orientation = 'bt-rl'
        #self.orientation = 'vertical'
        self.size_hint = (1, 1)
        self.padding = '40dp'
        self.spacing = '50dp'
        self.Time = TimeLabel()
        #self.TimeLayout = MDAnchorLayout(anchor_x = 'right', anchor_y = 'center')
        #self.TimeLayout.add_widget(self.Time)
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
        self.size_hint_y = 0.25
        self.Elapsed = MediaTimeElapsed()
        self.add_widget(self.Elapsed)
        self.Slider = MediaTimeSlider()
        self.add_widget(self.Slider)
        self.Left = MediaTimeLeft()
        self.add_widget(self.Left)

class MediaTimeSlider(MDSlider):

    def __init__(self, **kwargs):
        
        super(MediaTimeSlider, self).__init__(**kwargs)
        self.name = "MediaTimeSlider"
        self.range = (0, 1000)
        self.orientation = 'horizontal'
        self.step = 1
        self.value = 0
        self.show_off = False
        self.hint = False
        self.size_hint_x = 0.5
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

class MediaTimeElapsed(MDLabel):

    def __init__(self, **kwargs):
        
        super(MediaTimeElapsed, self).__init__(**kwargs)
        self.name = "MediaTimeElapsed"
        self.text = "0:00"
        self.font_style = 'H4'
        self.size_hint_x = 0.25
        self.halign = 'center'

class MediaTimeLeft(MDLabel):

    def __init__(self, **kwargs):
        
        super(MediaTimeLeft, self).__init__(**kwargs)
        self.name = "MediaTimeLeft"
        self.text = "-0:00"
        self.font_style = 'H4'
        self.size_hint_x = 0.25
        self.halign = 'center'

class MediaControlLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MediaControlLayout, self).__init__(**kwargs)
        self.name = "MediaControlLayout"
        self.orientation = 'horizontal'
        self.size_hint_y = 0.5
        self.spacing = "100dp"
        self.Back = MediaBackButton()
        self.add_widget(self.Back)
        self.Play = MediaPlayButton()
        self.add_widget(self.Play)
        self.Next = MediaNextButton()
        self.add_widget(self.Next)

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