from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from kivy.clock import Clock
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu

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
        self.spacing = "100dp"
        self.Zip = ZipCodeField()
        self.add_widget(self.Zip)
        self.Country = CountryCodeField()
        self.add_widget(self.Country)
        self.Units = UnitsField()
        self.add_widget(self.Units)

class ZipCodeField(MDTextField):

    def __init__(self, **kwargs):

        super(ZipCodeField, self).__init__(**kwargs)
        self.name = "ZipCodeField"
        self.hint_text = "Zip Code"
        self.text = "G1J3G2"
        self.helper_text = "No spaces"
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
        