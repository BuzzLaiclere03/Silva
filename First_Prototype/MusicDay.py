from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.image import AsyncImage
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
from datetime import datetime
from kivy.clock import Clock
import requests
import string
import coverpy
from gcsa.google_calendar import GoogleCalendar

from beautiful_date import Jan, Apr

class Day(MDGridLayout):

    def __init__(self, **kwargs):
        
        super(Day, self).__init__(**kwargs)
        self.name = "Day"
        self.orientation = 'vertical'
        self.size_hint = (1, 1)
        self.padding = '40dp'
        self.spacing = '50dp'

        self.calendar = GoogleCalendar('sarahmauderivard@gmail.com')

        Clock.schedule_interval(self.update_calendar, 60)

    def update_calendar(self, *args):
        # Called once a second using the kivy.clock module
        self.now = datetime.now()
        self.Time.text = self.now.strftime('%H:%M:%S')

        if self.Time.text == "00:00:00":
            self.Date.text = self.now.strftime("%A %d. %B %Y")

class MusicMainLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MusicMainLayout, self).__init__(**kwargs)
        self.name = "MusicMainLayout"
        self.orientation = 'horizontal'
        self.padding = "20dp"
        self.Artwork = MusicArtwork()
        self.add_widget(self.Artwork)
        self.InfoLayout = MusicInfoLayout()
        self.add_widget(self.InfoLayout)
        
        #self.size_hint_y = 0.25
        Clock.schedule_interval(self.Artwork.newArtwork, 1)

class MusicArtwork(AsyncImage):

    def __init__(self, **kwargs):
        
        super(MusicArtwork, self).__init__(**kwargs)
        self.name = "MusicArtwork"
        #self.size_hint = (1, 1)
        self.fit_mode = "contain"
        self.pos_hint = {"center_x":0.8, "center_y":0.5}
        self.coverpy = coverpy.CoverPy()
        self.showntitle = ""

    def newArtwork(self, dt):
        if self.showntitle != self.parent.InfoLayout.Title.Text.text :
            self.showntitle = self.parent.InfoLayout.Title.Text.text
            try:
                self.Temp = self.parent.InfoLayout.Album.Text.text + " " + self.parent.InfoLayout.Artist.Text.text
                print(self.Temp)
                self.result = self.coverpy.get_cover(self.Temp, 1)
                print(self.result.name)
                print(self.result.artwork(100))
                # Set a size for the artwork (first parameter) and get the result url.
                self.source = self.result.artwork()
            except requests.exceptions.HTTPError as f:
                print("Could not execute GET request")
                print(f)
            except Exception as e:
            	print("Nothing found.")
            
class MusicInfoLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MusicInfoLayout, self).__init__(**kwargs)
        self.name = "MusicInfoLayout"
        self.orientation = 'vertical'
        self.padding = (0, "100dp")
        self.Title = MusicTitle()
        self.add_widget(self.Title)
        self.Album = MusicAlbum()
        self.add_widget(self.Album)
        self.Artist = MusicArtist()
        self.add_widget(self.Artist)

class MusicTitle(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MusicTitle, self).__init__(**kwargs)
        self.name = "MusicTitle"
        self.orientation = 'horizontal'
        self.Text = DescText()
        self.add_widget(self.Text)

class DescText(MDLabel):

    def __init__(self, **kwargs):
        
        super(DescText, self).__init__(**kwargs)
        self.name = "DescText"
        self.font_style = 'H4'
        self.halign = 'center'
        self.size_hint_x = 0.7

class MusicAlbum(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MusicAlbum, self).__init__(**kwargs)
        self.name = "MusicAlbum"
        self.orientation = 'horizontal'
        self.Text = DescText()
        self.add_widget(self.Text)

class DescText(MDLabel):

    def __init__(self, **kwargs):
        
        super(DescText, self).__init__(**kwargs)
        self.name = "DescText"
        self.font_style = 'H4'
        self.halign = 'center'
        self.size_hint_x = 0.7

class MusicArtist(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MusicArtist, self).__init__(**kwargs)
        self.name = "MusicArtist"
        self.orientation = 'horizontal'
        self.Text = DescText()
        self.add_widget(self.Text)

class DescText(MDLabel):

    def __init__(self, **kwargs):
        
        super(DescText, self).__init__(**kwargs)
        self.name = "DescText"
        self.font_style = 'H4'
        self.halign = 'center'
        self.size_hint_x = 0.7