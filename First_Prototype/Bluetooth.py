from datetime import timedelta

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.core.window import Window

import kivy
kivy.require('1.10.0')

from kivy.uix.gridlayout import GridLayout
from kivy.properties import AliasProperty, BooleanProperty, NumericProperty, ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.logger import Logger

import pulsectl
import dbus

#from DBus import dbus.systemBus



'''
D-Bus stuff for accessing AVRCP through Bluez:
Name: org.bluez

Object path: /org/bluez/hci0/dev_B4_BF_F6_8C_FC_BF
Interface: org.bluez.MediaControl1
Methods:
- FastForward()
- Next()
- Pause()
- Play()
- Previous()
- Rewind()
- Stop()

Object path: /org/bluez/hci0/dev_B4_BF_F6_8C_FC_BF/player0
Interface: org.bluez.MediaPlayer1
Methods:
- FastForward()
- Next()
- Pause()
- Play()
- Previous()
- Rewind()
- Stop()
Properties:
- Repeat (boolean)
- Shuffle (boolean)
- Status (string; "paused" or similar)
- Track (dict of track info)
- Position (uint32)
'''

def renderMS(ms):
    return str(timedelta(milliseconds=ms))


class BTMusicDisplay(GridLayout):
    player_name = StringProperty()
    status = StringProperty()
    shuffle = BooleanProperty()
    repeat = BooleanProperty()
    position = NumericProperty()
    duration = NumericProperty()
    artist = StringProperty()
    album = StringProperty()
    track = StringProperty()
    volume = NumericProperty()

    def get_status_display(self):
        if self.duration:
            return f'{self.status.capitalize()} ({renderMS(self.position)[:-5]} / {renderMS(self.duration)})'
        return self.status

    status_display = AliasProperty(get_status_display, None, bind=('status', 'position', 'duration'))

    def __init__(self, **kwargs):
        super(BTMusicDisplay, self).__init__(**kwargs)
        self.pulse = pulsectl.Pulse('karvy')
        self.pulse.event_mask_set('all')
        self.pulse.event_callback_set(self.printPAEvent)
        #self.volume = self.pulse.sink_input_list()[0].volume.value_flat
        self.refreshBTDevice()

        self.triggerRefreshBTDevice = Clock.create_trigger(self.refreshBTDevice)
        self.triggerUpdate = Clock.create_trigger(self.checkUpdate)

        Clock.schedule_interval(self.triggerUpdate, 0.01)

    def printPAEvent(self, ev):
        Logger.info(f'BTMusicDisplay: Pulse event: {ev}')
        #self.volume = self.pulse.sink_input_list()[0].volume.value_flat

    def refreshBTDevice(self, *args):
        rootBTObj = dbus.systemBus.get_object('org.bluez', '/')
        managedObjects = rootBTObj.GetManagedObjects(dbus_interface='org.freedesktop.DBus.ObjectManager')

        self.playerObjectPath = None
        self.player = None

        for path in managedObjects:
            if path.endswith('/player0'):
                Logger.info(f'BTMusicDisplay: Found media player: {path}')

                self.playerObjectPath = path

                deviceObject = dbus.systemBus.get_object('org.bluez', self.playerObjectPath[:-8])
                self.player_name = deviceObject.Get(
                    'org.bluez.Device1',
                    'Alias',
                    dbus_interface='org.freedesktop.DBus.Properties'
                )

                self.player = dbus.Interface(
                    dbus.systemBus.get_object('org.bluez', self.playerObjectPath),
                    dbus_interface='org.bluez.MediaPlayer1',
                )
                self.playerPropsDevice = dbus.Interface(
                    dbus.systemBus.get_object('org.bluez', self.playerObjectPath),
                    dbus_interface='org.freedesktop.DBus.Properties',
                )

                self.checkUpdate()

    def catchDBusErrors(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except dbus.exceptions.DBusException as err:
                Logger.warn(f'BTMusicDisplay: DBus error while calling {func.__name__}: {err}')
                self.setDefaultValues()
                self.triggerRefreshBTDevice()
        wrapper.__name__ = func.__name__
        return wrapper

    def getPlayer(self):
        dbus.systemBus.get_object('org.bluez', self.playerObjectPath)

    @catchDBusErrors
    def previous(self):
        self.player and self.player.Previous()

    @catchDBusErrors
    def next(self):
        self.player and self.player.Next()

    @catchDBusErrors
    def play(self):
        self.player and self.player.Play()

    @catchDBusErrors
    def pause(self):
        self.player and self.player.Pause()

    @catchDBusErrors
    def toggle_shuffle(self):
        self.setPlayerProp('Shuffle', 'off' if self.shuffle else 'alltracks')

    @catchDBusErrors
    def toggle_repeat(self):
        self.setPlayerProp('Repeat', 'off' if self.repeat else 'alltracks')

    def getPlayerProp(self, name):
        return self.playerPropsDevice and self.playerPropsDevice.Get('org.bluez.MediaPlayer1', name)

    def setPlayerProp(self, name, value):
        self.playerPropsDevice and self.playerPropsDevice.Set('org.bluez.MediaPlayer1', name, value)

    def setDefaultValues(self):
        self.status = 'disconnected'
        self.position = 0
        self.duration = 0
        self.artist = '-'
        self.album = '-'
        self.track = '-'

    @catchDBusErrors
    def checkUpdate(self, *args):
        if self.playerObjectPath is None or self.player is None:
            self.setDefaultValues()
            self.triggerRefreshBTDevice()
            return

        self.status = self.getPlayerProp('Status')
        self.position = int(self.getPlayerProp('Position'))
        self.shuffle = self.getPlayerProp('Shuffle') != 'off'
        self.repeat = self.getPlayerProp('Repeat') != 'off'

        track = self.getPlayerProp('Track')
        self.duration = int(track['Duration'])
        self.artist = track.get('Artist', '-')
        self.album = track.get('Album', '-')
        self.track = track.get('Title', '-')

        self.pulse.event_listen(timeout=0.001)

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        Builder.load_string(
'''    
#:kivy 1.10.0
   
<TrackDisplay@Label>:
    font_size: 50

<MetadataDisplay@Label>:
    font_size: 20
    height: 24
    size_hint_y: None
    valign: 'middle'

<TransportButton@Button>:
    font_size: 60
    markup: True
    background_color: 0.4, 0.4, 0.4, 0.7
    
<TransportToggleButton@ToggleButton>:
    font_size: 60
    markup: True
    background_color: 0.4, 0.4, 0.4, 0.7
    
<Screen>:
    BTMusicDisplay:
        cols: 1
        padding: 20
    
        Label:
            text: root.player_name
            size: self.texture_size
            size_hint_y: None
    
        TrackDisplay:
            text: root.track
    
        MetadataDisplay:
            text: 'Artist: {}'.format(root.artist)
    
        MetadataDisplay:
            text: 'Album: {}'.format(root.album)
    
        BoxLayout:
            height: 40
            size_hint_y: None
    
            padding: 1, 8, 1, 10
    
            Label:
                markup: True
                font_size: 14
                text: root.status_display
                outline_color: 0, 0, 0, 0.5
                outline_width: 2

                canvas.before:
                    Color:
                        rgba: 0.1, 0.1, 0.1, 0.5
                    Rectangle:
                        pos: self.pos
                        size: self.width, self.height
    
                    Color:
                        rgba: 0, 0.7, 0, 0.7
                    Rectangle:
                        pos: self.pos
                        size: self.width * (root.position / (root.duration or 1)), self.height
    
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.5
    
            TransportToggleButton:
                state: 'down' if root.shuffle else 'normal'
                on_press: root.toggle_shuffle()
    
            TransportButton:
                on_press: root.previous()
    
            TransportButton:
                on_press: root.pause()
    
            TransportButton:
                on_press: root.play()
    
            TransportButton:
                on_press: root.next()
    
            TransportToggleButton:
                state: 'down' if root.repeat else 'normal'
                on_press: root.toggle_repeat()
'''
)

MainApp().run()