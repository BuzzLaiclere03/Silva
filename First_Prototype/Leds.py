from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from kivymd.uix.pickers import MDColorPicker
#from rgbw_colorspace_converter import RGB
from kivy.graphics import Color

class LedsMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(LedsMenu, self).__init__(**kwargs)
        self.name = "LedsMenu"
        self.text = "Leds"
        self.icon = "lightbulb"
        self.Layout = LedsLayout()
        self.add_widget(self.Layout)

class LedsLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(LedsLayout, self).__init__(**kwargs)
        self.name = "LedsLayout"
        self.orientation = 'horizontal'
        self.Selection = ColorLayout()
        self.add_widget(self.Selection)

class ColorLayout(MDGridLayout):

    def __init__(self, **kwargs):
        
        super(ColorLayout, self).__init__(**kwargs)
        self.name = "LedsLayout"
        #self.cols_minimum = 2
        #self.rows_minimum = 2
        self.Color1 = ColorSelected()
        self.add_widget(self.Color1)

class ColorSelected(MDIconButton):

    def __init__(self, **kwargs):
        
        super(ColorSelected, self).__init__(**kwargs)
        self.name = "ColorSelected"
        self.icon = "checkbox-blank-circle-outline"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.size_hint_x = 0.5
        self.icon_size = "75dp"
        self.on_press = self.update
        #self.theme_icon_color: "Custom"
        self.icon_color = Color(1, 1, 1)

    def update(self):
        Debug.Start("ColorSelected -> Pressed")
        self.icon = "checkbox-marked-circle"
        Debug.Log(f"Selected Color is now {self.icon_color}")
        self.parent.RGB.icon = "checkbox-blank-circle-outline"
        Debug.End()



'''
class LedsLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(LedsLayout, self).__init__(**kwargs)
        self.name = "LedsLayout"
        self.orientation = 'horizontal'
        self.Selection = TypeSelected()
        self.add_widget(self.Selection)

class TypeSelected(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(TypeSelected, self).__init__(**kwargs)
        self.name = "TypeSelected"
        self.orientation = 'vertical'
        self.White = WhiteSelected()
        self.add_widget(self.White)
        self.RGB = RGBSelected()
        self.add_widget(self.RGB)

class WhiteSelected(MDIconButton):

    def __init__(self, **kwargs):
        
        super(WhiteSelected, self).__init__(**kwargs)
        self.name = "WhiteSelected"
        self.icon = "checkbox-marked-circle"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.size_hint_x = 0.5
        self.icon_size = "75dp"
        self.on_press = self.update

    def update(self):
        Debug.Start("WhiteSelected -> Pressed")
        self.icon = "checkbox-marked-circle"
        Debug.Log("Base Color is now white")
        self.parent.RGB.icon = "checkbox-blank-circle-outline"
        Debug.End()

class RGBSelected(MDIconButton):

    def __init__(self, **kwargs):
        
        super(RGBSelected, self).__init__(**kwargs)
        self.name = "RGBSelected"
        self.icon = "checkbox-blank-circle-outline"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.size_hint_x = 0.5
        self.icon_size = "75dp"
        self.on_press = self.update

    def update(self):
        Debug.Start("RGBSelected -> Pressed")
        self.icon = "checkbox-marked-circle"
        Debug.Log("Base Color is now rgb")
        self.parent.White.icon = "checkbox-blank-circle-outline"
        Debug.End()

class HueSlider(MDSlider):

    def __init__(self, **kwargs):
        
        super(HueSlider, self).__init__(**kwargs)
        self.name = "HueSlider"
        self.range = (0, 1000)
        self.orientation = 'horizontal'
        self.step = 1
        self.value = 0
        self.show_off = False
        self.hint = False
        self.size_hint_x = 0.5
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        '''


class ColorSelection(MDColorPicker):

    def __init__(self, **kwargs):
        
        super(ColorSelection, self).__init__(**kwargs)
