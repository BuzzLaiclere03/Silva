from kivymd.app import MDApp
import json
import os
import pathlib
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton


class MyLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        super(MDBoxLayout, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0)
        self.adaptive_size = False
        self.padding = [50, 50, 50, 50]
        self.spacing= 50
        self.MyButton = MDRectangleFlatButton(on_press = self.add, text = "+1", size_hint = (0.5,0.5), pos_hint = {"center_x":0.5, "center_y":0.5})
        self.add_widget(self.MyButton)
        self.MyLabel = MDLabel(size_hint = (0.5,0.5), text = '0', pos_hint = {"center_x":0.5, "center_y":0.5})
        self.add_widget(self.MyLabel)

    def add(self, xd):
        # Open the file for reading
        with open('Data.json', 'r') as f:
            data = json.load(f)

        data['number'] += 1

        # Open the file for writing
        with open('Data.json', 'w') as f:
            json.dump(data, f)

        # Close the file
        f.close()

    def update(self, dt):
        # Open the file for reading
        with open('Data.json', 'r') as f:
            data = json.load(f)

        # Do some processing with the data
        self.MyLabel.text = str(data['number'])

        # Close the file
        f.close()


class MyScreen(MDScreen):

    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.layout = MyLayout()
        self.add_widget(self.layout)     

class Example(MDApp):

    def build(self):
        print(pathlib.Path(__file__).parent.resolve())
        os.chdir(pathlib.Path(__file__).parent.resolve())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MyScreen()

if __name__ == '__main__':
    Example().run()