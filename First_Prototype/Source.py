from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from kivy.clock import Clock

class SourceMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(SourceMenu, self).__init__(**kwargs)
        self.name = "SourceMenu"
        self.text = "Source"
        self.icon = "bluetooth"
        self.MainLayout = SourceMainLayout()
        self.add_widget(self.MainLayout)

class SourceMainLayout(MDBoxLayout):

    def __init__(self, **kwargs):

        super(SourceMainLayout, self).__init__(**kwargs)
        self.name = "SourceLayout"
        self.orientation = 'horizontal'
        self.NewSource = ""
        self.Bass = EQLayout()
        self.Bass.Name.text = "B"
        self.add_widget(self.Bass)
        self.Mid = EQLayout()
        self.Mid.Name.text = "M"
        self.add_widget(self.Mid)
        self.Treble = EQLayout()
        self.Treble.Name.text = "T"
        self.add_widget(self.Treble)
        #self.RPi = SourceRPiLayout()
        #self.add_widget(self.RPi)

class EQLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(EQLayout, self).__init__(**kwargs)
        self.name = "SourceRPiLayout"
        self.orientation = 'vertical'
        self.size_hint_y = 1
        self.spacing = "10dp"
        self.padding = "100dp"
        self.Slider = EQSlider()
        self.add_widget(self.Slider)
        self.Name = EQName()
        self.add_widget(self.Name)

class EQSlider(MDSlider):

    def __init__(self, **kwargs):
        
        super(EQSlider, self).__init__(**kwargs)
        self.name = "EQSlider"
        self.range = (0, 255)
        self.orientation = 'vertical'
        self.step = 1
        self.value = 127
        self.show_off = False
        self.hint = False
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x":0.5, "center_y":0.4}

class EQName(MDLabel):

    def __init__(self, **kwargs):
        
        super(EQName, self).__init__(**kwargs)
        self.name = "EQName"
        self.text= ""
        self.halign = "center"
        self.font_style = "H3"
        self.pos_hint_y = 1
        self.size_hint_y = 0.15

class SourceRPiLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(SourceRPiLayout, self).__init__(**kwargs)
        self.name = "SourceRPiLayout"
        self.orientation = 'vertical'
        self.size_hint_y = 1
        self.spacing = "10dp"
        self.padding = ["0dp", "300dp"]
        self.DeviceName = RPiDeviceName()
        self.add_widget(self.DeviceName)
        self.Bluetooth = RPiBtConnection()
        self.add_widget(self.Bluetooth)

class RPiDeviceName(MDLabel):

    def __init__(self, **kwargs):
        
        super(RPiDeviceName, self).__init__(**kwargs)
        self.name = "RPiDeviceName"
        self.text= "No device connected"
        self.halign = "center"
        self.font_style = "H4"
        self.pos_hint_x = 0.5

class RPiBtConnection(MDIconButton):

    def __init__(self, **kwargs):
        
        super(RPiBtConnection, self).__init__(**kwargs)
        self.name = "RPiBtConnection"
        self.size_hint_x = 0.5 
        self.pos_hint = {"center_x":0.5, "top":0}
        self.on_press = self.Pressed
        self.icon = "bluetooth"
        self.icon_size = "150dp"

    def Pressed(self):

        Debug.Start("RPiBtConnection -> Pressed")
        SourceMainLayout.NewSource = "RPi"
        Debug.End()