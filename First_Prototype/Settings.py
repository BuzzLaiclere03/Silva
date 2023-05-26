from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from kivy.clock import Clock
from kivymd.uix.textfield import MDTextField

class SettingsMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(SettingsMenu, self).__init__(**kwargs)
        self.name = "SettingsMenu"
        self.text = "Settings"
        self.icon = "cog"
        self.Layout = SettingsMainLayout()
        self.add_widget(self.Layout)

class SettingsMainLayout(MDBoxLayout):

    def __init__(self, **kwargs):

        super(SettingsMainLayout, self).__init__(**kwargs)
        self.name = "SettingsMainLayout"
        self.orientation = 'vertical'
        self.padding = "100dp"
        #self.spacing = "100dp"
        #self.size_hint = (1, 1)
        
        self.CityLayout = MDAnchorLayout(size_hint = (1, 1))
        self.CityLayout.City = CityCodeField()
        self.CityLayout.add_widget(self.CityLayout.City)
        self.add_widget(self.CityLayout)
        
        self.CountryLayout = MDAnchorLayout(size_hint = (1, 1))
        self.CountryLayout.Country = CountryCodeField()
        self.CountryLayout.add_widget(self.CountryLayout.Country)
        self.add_widget(self.CountryLayout)
        
        self.UnitsLayout = MDAnchorLayout(size_hint = (1, 1))
        self.UnitsLayout.Units = UnitsField()
        self.UnitsLayout.add_widget(self.UnitsLayout.Units)
        self.add_widget(self.UnitsLayout)
        
class CityCodeField(MDTextField):

    def __init__(self, **kwargs):

        super(CityCodeField, self).__init__(**kwargs)
        self.name = "CityCodeField"
        self.hint_text = "City Code"
        self.text = "Quebec"
        self.helper_text = "Name of your city"
        self.helper_text_mode = "on_error"
        self.required = True
        self.max_text_length = 6
        self.size_hint = (1, None)
        self.halign = "left"

class CountryCodeField(MDTextField):

    def __init__(self, **kwargs):

        super(CountryCodeField, self).__init__(**kwargs)
        self.name = "CountryCodeField"
        self.hint_text = "Country Code"
        self.text = "ca"
        self.helper_text = "Canada = ca, USA = us, etc."
        self.helper_text_mode = "on_error"
        self.required = True
        self.max_text_length = 2
        self.size_hint = (1, None)
        self.halign = "left"

class UnitsField(MDTextField):

    def __init__(self, **kwargs):

        super(UnitsField, self).__init__(**kwargs)
        self.name = "UnitsField"
        self.hint_text = "Units"
        self.text = "metric"
        self.helper_text = "C = metric, F = imperial, K = kelvin"
        self.helper_text_mode = "on_error"
        self.required = True
        self.max_text_length = 8
        self.size_hint = (1, None)
        self.halign = "left"
        