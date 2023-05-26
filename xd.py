from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.slider import MDSlider

def on_touch_down(*args):
    print("on_touch_down")

def on__is_off(*args):
    print("on__is_off")

def on_value_normalized(*args):
    print("on_value_normalized")

def on_hint(*args):
    print("on_hint")



class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.slider = MDSlider(min=0, max=100, value=50)
        self.slider.step = 5
        self.slider.bind(value = self.on_sus)

        layout.add_widget(self.slider)
        self.add_widget(layout)
    
    def on_sus(self, *args):
        print(self.slider.value)


class SimpleApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        main_screen = MainScreen(name='main')
        screen_manager.add_widget(main_screen)
        return screen_manager


if __name__ == '__main__':
    SimpleApp().run()













#from kivy.lang import Builder
#from kivy.metrics import dp
#from kivy.uix.button import Button
#from kivymd.app import MDApp
#
#KV = """
#<RoundButton>:
#    size_hint: None, None
#    size: dp(56), dp(56)
#    canvas.before:
#        Ellipse:
#            pos: self.pos
#            size: self.size
#"""
#
#class RoundButton(Button):
#    pass
#
#class RoundButtonApp(MDApp):
#    def build(self):
#        return Builder.load_string(KV)
#
#RoundButtonApp().run()
