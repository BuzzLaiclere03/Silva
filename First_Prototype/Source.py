from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
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
        self.orientation = 'vertical'
        self.RPi = SourceRPiLayout()
        self.add_widget(self.RPi)
        self.ESP = SourceESPLayout()
        self.add_widget(self.ESP)
        self.Selected = "RPi"
        self.NewSource = ""

class SourceRPiLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(SourceRPiLayout, self).__init__(**kwargs)
        self.name = "SourceRPiLayout"
        self.orientation = 'horizontal'
        self.size_hint_y = 0.5
        self.spacing = "10dp"
        self.Select = RPiSelected()
        self.add_widget(self.Select)
        self.Name = MDLabel(text = "Rpi :", font_style = "H4", size_hint_x = 0.35)
        self.add_widget(self.Name)
        self.DeviceName = RPiDeviceName()
        self.add_widget(self.DeviceName)
        self.Bluetooth = RPiBtConnection()
        self.add_widget(self.Bluetooth)

class RPiSelected(MDIconButton):

    def __init__(self, **kwargs):
        
        super(RPiSelected, self).__init__(**kwargs)
        self.name = "RPiSelected"
        self.icon = "checkbox-marked-circle"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.size_hint_x = 0.5
        self.icon_size = "75dp"
        self.on_press = self.update

    def update(self):
        Debug.Start("RPiSelected -> Pressed")
        SourceMainLayout.Selected = "RPi"
        self.icon = "checkbox-marked-circle"
        Debug.Log("Source is now RPi")
        #self.root.root.ESP.Select.icon = "checkbox-blank-circle-outline"
        self.parent.parent.ESP.Select.icon = "checkbox-blank-circle-outline"
        Debug.End()

class RPiDeviceName(MDLabel):

    def __init__(self, **kwargs):
        
        super(RPiDeviceName, self).__init__(**kwargs)
        self.name = "RPiDeviceName"
        self.text= "No device connected"
        self.halign = "left"
        self.font_style = "H5"
        self.size_hint_x = 0.8

class RPiBtConnection(MDIconButton):

    def __init__(self, **kwargs):
        
        super(RPiBtConnection, self).__init__(**kwargs)
        self.name = "RPiBtConnection"
        self.size_hint_x = 0.8 
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.on_press = self.Pressed
        self.icon = "bluetooth"
        self.icon_size = "75dp"

    def Pressed(self):

        Debug.Start("RPiBtConnection -> Pressed")
        SourceMainLayout.NewSource = "RPi"
        Debug.End()

class SourceESPLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(SourceESPLayout, self).__init__(**kwargs)
        self.name = "SourceESPLayout"
        self.orientation = 'horizontal'
        self.size_hint_y = 0.5
        self.spacing = "10dp"
        self.Select = ESPSelected()
        self.add_widget(self.Select)
        self.Name = MDLabel(text = "ESP :", font_style = "H4", size_hint_x = 0.35)
        self.add_widget(self.Name)
        self.DeviceName = ESPDeviceName()
        self.add_widget(self.DeviceName)
        self.Bluetooth = ESPBtConnection()
        self.add_widget(self.Bluetooth)

class ESPSelected(MDIconButton):

    def __init__(self, **kwargs):
        
        super(ESPSelected, self).__init__(**kwargs)
        self.name = "ESPSelected"
        self.icon = "checkbox-blank-circle-outline"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.size_hint_x = 0.5
        self.icon_size = "75dp"
        self.on_press = self.update

    def update(self):
        Debug.Start("ESPSelected -> Pressed")
        SourceMainLayout.Selected = "ESP"
        self.icon = "checkbox-marked-circle"
        Debug.Log("Source is now ESP")
        self.parent.parent.RPi.Select.icon = "checkbox-blank-circle-outline"
        Debug.End()

class ESPDeviceName(MDLabel):

    def __init__(self, **kwargs):
        
        super(ESPDeviceName, self).__init__(**kwargs)
        self.name = "ESPDeviceName"
        self.text= "No device connected"
        self.halign = "left"
        self.font_style = "H5"
        self.size_hint_x = 0.8

class ESPBtConnection(MDIconButton):

    def __init__(self, **kwargs):
        
        super(ESPBtConnection, self).__init__(**kwargs)
        self.name = "ESPBtConnection"
        self.size_hint_x = 0.8
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.on_press = self.Pressed
        self.icon = "bluetooth"
        self.icon_size = "75dp"

    def Pressed(self):

        Debug.Start("ESPBtConnection -> Pressed")
        SourceMainLayout.NewSource = "ESP"
        Debug.End()