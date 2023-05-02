from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from kivy.clock import Clock

class SettingsMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(SettingsMenu, self).__init__(**kwargs)
        self.name = "SettingsMenu"
        self.text = "Settings"
        self.icon = "cog"
        self.label = MDLabel(text='Settings', halign='center')
        self.add_widget(self.label)