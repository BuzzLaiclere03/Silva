from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.button import MDIconButton
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from kivymd.uix.pickers import MDColorPicker
from kivy.graphics import Color
from typing import Union
from kivy.utils import get_color_from_hex, get_hex_from_color
import time

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
        self.Selection = SelectionLayout()
        self.ColorPicker = ColorSelection(self.Selection)
        self.add_widget(self.Selection)
        self.Setting = ColorSettings()
        self.add_widget(self.Setting)


class ColorSelection(MDColorPicker):

    def __init__(self, Selection, **kwargs):
        
        super(ColorSelection, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.SelectedButtons = Selection
        self.on_release = self.get_selected_color

    def get_selected_color(
        self,
        instance_color_picker: MDColorPicker,
        selected_color: Union[list, str]
    ):
        
        #Return selected color
        print(f"Selected color is {selected_color}")
        for self.colorbuttons in self.SelectedButtons.children:
            if self.colorbuttons.icon == "checkbox-marked-circle":
                self.colorbuttons.icon_color = selected_color
 
        self.dismiss()

class SelectionLayout(MDGridLayout):

    def __init__(self, **kwargs):
        
        super(SelectionLayout, self).__init__(**kwargs)
        self.name = "LedsLayout"
        self.cols = 2
        self.rows = 2
        self.size_hint = (1, 1)
        self.Color1 = ColorSelected("Color1")
        self.add_widget(self.Color1)
        self.Color2 = ColorSelected("Color2")
        self.add_widget(self.Color2)
        self.Color3 = ColorSelected("Color3")
        self.add_widget(self.Color3)
        self.Color4 = ColorSelected("Color4")
        self.add_widget(self.Color4)

    def updateChilds(self, childcalled):
        Debug.Start("ColorSelected -> Pressed")
        for self.child in self.children:
            if self.child.name == childcalled:
                self.child.icon = "checkbox-marked-circle"
                Debug.Log(f"Selected Color is now {self.child.icon_color}")
            else:
                self.child.icon = "checkbox-blank-circle-outline"
        Debug.End()


class ColorSelected(MDIconButton):

    def __init__(self, number, **kwargs):
        
        super(ColorSelected, self).__init__(**kwargs)
        self.name = number
        self.icon = "checkbox-blank-circle-outline"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.size_hint = (1, 1)
        self.icon_size = "75dp"
        self.Selection = "#FFFFFF"
        self.on_press = self.update
        self.theme_icon_color = "Custom"
        self.icon_color  = get_color_from_hex(self.Selection)


    def update(self):
        self.parent.updateChilds(self.name)

class ColorSettings(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(ColorSettings, self).__init__(**kwargs)
        self.name = "ColorSettings"
        self.orientation = 'vertical'
        self.size_hint = (1, 1)
        self.Layout = ColorLayout()
        self.add_widget(self.Layout)
        self.Buttons = ColorButton()
        self.add_widget(self.Buttons)

    def updateChilds(self, childcalled):
        Debug.Start("ColorSelected -> Pressed")
        for self.child in self.children:
            if self.child.name == childcalled:
                self.child.icon = "checkbox-marked-circle"
                Debug.Log(f"Selected Color is now {self.child.icon_color}")
            else:
                self.child.icon = "checkbox-blank-circle-outline"
        Debug.End()

class ColorLayout(MDAnchorLayout):

    def __init__(self, **kwargs):
        
        super(ColorLayout, self).__init__(**kwargs)
        self.name = "ColorLayout"
        self.anchor_y = 'bottom'
        self.size_hint = (1, 1)
        self.Color = ColorChoosed()
        self.add_widget(self.Color)

class ColorChoosed(MDIconButton):

    def __init__(self, **kwargs):
        
        super(ColorChoosed, self).__init__(**kwargs)
        self.name = "ColorChoosed"
        self.size_hint = (0.7, 0.7)
        self.Selection = "#FFFFFF"
        self.theme_icon_color = "Custom"
        self.icon = "lightbulb-outline"
        self.icon_size = "300dp"
        self.icon_color = get_color_from_hex(self.Selection)
        self.on_press = self.update
        self.start = time.time()

    def update(self):
        self.end = time.time()

        if((self.end - self.start) > 0.5):

            self.start = time.time()
            if self.icon == "lightbulb-outline":
                self.icon = "lightbulb"
            elif self.icon == "lightbulb":
                self.icon = "lightbulb-outline"

class ColorButton(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(ColorButton, self).__init__(**kwargs)
        self.name = "ColorButton"
        self.orientation = 'horizontal'
        self.Change = ChangeColorButton()
        self.add_widget(self.Change)
        self.Apply = ApplyChanges()
        self.add_widget(self.Apply)

class ChangeColorButton(MDIconButton):

    def __init__(self, **kwargs):
        
        super(ChangeColorButton, self).__init__(**kwargs)
        self.name = "ChangeColorButton"
        self.icon = "pencil-circle"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.size_hint = (1, 1)
        self.icon_size = "75dp"
        self.Selection = "#FFFFFF"
        self.on_press = self.ChangeColor
        self.theme_icon_color = "Custom"
        self.icon_color = get_color_from_hex(self.Selection)

    def ChangeColor(self):
        self.parent.parent.parent.ColorPicker.open()

class ApplyChanges(MDIconButton):

    def __init__(self, **kwargs):
        
        super(ApplyChanges, self).__init__(**kwargs)
        self.name = "ApplyChanges"
        self.icon = "check-underline-circle"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.size_hint = (1, 1)
        self.icon_size = "75dp"
        self.Selection = "#FFFFFF"
        self.on_press = self.update
        self.theme_icon_color = "Custom"
        self.icon_color = "green"


    def update(self):
        for colorbuttons in self.parent.parent.parent.Selection.children:
            if colorbuttons.icon == "checkbox-marked-circle":
                self.parent.parent.Layout.Color.icon_color = colorbuttons.icon_color


