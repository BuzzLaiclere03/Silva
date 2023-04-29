from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
        
class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        
        super(MDScreen, self).__init__(**kwargs)
        self.nav = Menu()
        self.add_widget(self.nav)

class Menu(MDBottomNavigation):
    
    def __init__(self, **kwargs):
        
        super(MDBottomNavigation, self).__init__(**kwargs)

class MediaMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MDBottomNavigation, self).__init__(**kwargs)
        self.name = "MediaMenu"
        self.text = "Media"
        self.icon = ""
