from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.spinner import MDSpinner

class Example(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"

        return Builder.load_file('main.kv')

Example().run()