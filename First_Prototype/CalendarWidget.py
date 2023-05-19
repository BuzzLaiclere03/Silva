from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRectangleFlatButton
from datetime import datetime
import calendar

Builder.load_string(
'''
<CalendarWidget>:
    orientation: 'vertical'
    spacing: '2dp'
    padding: '40dp'
    MDBoxLayout:
        size_hint_y: None
        height: self.minimum_height
        orientation: 'horizontal'
        padding: '4dp'
        spacing: '4dp'
    GridLayout:
        id: calendar_grid
        cols: 7
        spacing: '2dp'
        padding: '2dp'
''')

class CalendarWidget(MDBoxLayout):
    selected_date = ObjectProperty()
    month = NumericProperty()
    year = NumericProperty()

    def __init__(self, **kwargs):
        super(CalendarWidget, self).__init__(**kwargs)
        calendar.setfirstweekday(calendar.SUNDAY)
        self.selected_date = None
        self.update_calendar()

    def update_calendar(self):
        self.ids.calendar_grid.clear_widgets()

        self.today = datetime.now().date()
        self.month = self.today.month
        self.year = self.today.year

        week_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

        for week_day in week_days:
            label = MDLabel(text=week_day, size_hint=(1, None), height="40dp", halign = "center", font_style = "H5")
            self.ids.calendar_grid.add_widget(label)

        self.thismonth = calendar.monthcalendar(self.year, self.month)
        #print(self.thismonth)
        # Adjust the position of the days based on the starting weekday
        for Week in self.thismonth:
            for day in Week:
                if day == 0:
                    self.ids.calendar_grid.add_widget(MDLabel(disabled=True))
                else:
                    self.labelday = MDLabel(text=str(day), halign = "center", font_style = "H5")
                    if day == self.today.day:
                        self.labelday = MDRectangleFlatButton(text=str(day), halign = "center", font_style = "H5", line_width = "3dp", line_color = (1, 1, 1, 1), text_color = (1, 1, 1, 1), pos_hint = {"center_x":0.5, "center_y":0.5}, size_hint = (0.5, 0.5))
                    #else:
                    self.ids.calendar_grid.add_widget(self.labelday)


class MediaWidget(MDBoxLayout):

    def __init__(self, **kwargs):
        super(CalendarWidget, self).__init__(**kwargs)
        calendar.setfirstweekday(calendar.SUNDAY)
        self.selected_date = None
        self.today = datetime.now().date()
        self.month = self.today.month
        self.year = self.today.year
        self.update_calendar()

    def update_calendar(self):
        self.ids.calendar_grid.clear_widgets()

        week_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

        for week_day in week_days:
            label = MDLabel(text=week_day, size_hint=(1, None), height="40dp", halign = "center", font_style = "H5")
            self.ids.calendar_grid.add_widget(label)

        self.thismonth = calendar.monthcalendar(self.year, self.month)
        #print(self.thismonth)
        # Adjust the position of the days based on the starting weekday
        for Week in self.thismonth:
            for day in Week:
                if day == 0:
                    self.ids.calendar_grid.add_widget(MDLabel(disabled=True))
                else:
                    self.labelday = MDLabel(text=str(day), halign = "center", font_style = "H5")
                    if day == self.today.day:
                        self.labelday = MDRectangleFlatButton(text=str(day), halign = "center", font_style = "H5", line_width = "3dp", line_color = (1, 1, 1, 1), text_color = (1, 1, 1, 1), pos_hint = {"center_x":0.5, "center_y":0.5}, size_hint = (0.5, 0.5))
                    #else:
                    self.ids.calendar_grid.add_widget(self.labelday)


