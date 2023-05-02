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
        self.Zip = ZipCodeField()
        self.add_widget(self.Zip)
        self.Country = CountryCodeField()
        self.add_widget(self.Country)
        self.Units = UnitsLayout()
        self.add_widget(self.Units)

class ZipCodeField(MDTextField):

    def __init__(self, **kwargs):

        super(ZipCodeField, self).__init__(**kwargs)
        self.name = "ZipCodeField"
        self.hint_text = "Zip Code"
        self.helper_text = "No spaces"
        self.helper_text_mode = "on_focus"

class CountryCodeField(MDTextField):

    def __init__(self, **kwargs):

        super(CountryCodeField, self).__init__(**kwargs)
        self.name = "CountryCodeField"
        self.hint_text = "Country Code"
        self.helper_text = "Canada = ca, USA = us, etc."
        self.helper_text_mode = "on_focus"

class UnitsLayout(MDBoxLayout):

    def __init__(self, **kwargs):

        super(UnitsLayout, self).__init__(**kwargs)
        self.name = "UnitsLayout"
        self.orientation = 'horizontal'
        self.Label = MDLabel(text = "Units :", font_style = "H5")
        self.add_widget(self.Label)
        self.Selected = UnitsSelection()
        self.add_widget(self.Selected)

class UnitsSelection(MDDropDownItem):

    def __init__(self, **kwargs):

        super(UnitsSelection, self).__init__(**kwargs)
        self.name = "UnitsSelection"
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.AvailableUnits = ['C', 'F', 'K']
        self.menu_items = [
            {
                "text": units,
                "height": 56,
                "on_release": lambda x = units: self.SetNewUnits(x),
            } for units in self.AvailableUnits
        ]
        self.menu = MDDropdownMenu(
            caller = self,
            items = self.menu_items,
            position = "top",
        )
        self.menu.bind()

    def SetNewUnits(self, units):
        Debug.Start("SetNewUnits")
        Debug.Log(f"Loading new selected units: {units}")
        self.menu.dismiss()
        Debug.End()
        pass
        