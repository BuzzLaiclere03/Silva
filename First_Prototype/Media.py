from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug

class MediaMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MediaMenu, self).__init__(**kwargs)
        self.name = "MediaMenu"
        self.text = "Media"
        self.icon = "music-box"
        self.MainLayout = MediaLayout()
        self.add_widget(self.MainLayout)

class MediaLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MediaLayout, self).__init__(**kwargs)
        self.name = "MediaLayout"
        self.orientation = 'vertical'
        self.MediaTime = MediaTimeLayout()
        self.add_widget(self.MediaTime)
        self.MediaControl = MediaControlLayout()
        self.add_widget(self.MediaControl)
        self.MediaVolume = MediaVolumeLayout()
        self.add_widget(self.MediaVolume)

class MediaTimeLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MediaTimeLayout, self).__init__(**kwargs)
        self.name = "MediaTimeLayout"
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

class MediaBackButton(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaBackButton, self).__init__(**kwargs)
        self.name = "MediaBackButton"
        self.icon = "skip-previous"
        self.icon_size = "75dp"
        self.size_hint = (0.3,0.3) 
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

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
        self.value = 50
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