from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.button import Button
from kivymd.app import MDApp

KV = """
<RoundButton>:
    size_hint: None, None
    size: dp(56), dp(56)
    canvas.before:
        Ellipse:
            pos: self.pos
            size: self.size
"""

class RoundButton(Button):
    pass

class RoundButtonApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

RoundButtonApp().run()
