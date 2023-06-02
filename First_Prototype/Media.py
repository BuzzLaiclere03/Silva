from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from BRS_Python_Libraries.BRS.Debug.consoleLog import Debug
import time

from kivy.clock import Clock
import pulsectl
import dbus

systembus = dbus.SystemBus()

class MediaMenu(MDBottomNavigationItem):

    def __init__(self, **kwargs):
        
        super(MediaMenu, self).__init__(**kwargs)
        self.name = "MediaMenu"
        self.text = "Media"
        self.icon = "music-box"
        self.Layout = MediaLayout()
        self.add_widget(self.Layout)

class MediaLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MediaLayout, self).__init__(**kwargs)
        self.name = "MediaLayout"
        self.orientation = 'vertical'
        self.Time = MediaTimeLayout()
        self.add_widget(self.Time)
        self.Control = MediaControlLayout()
        self.add_widget(self.Control)
        self.Volume = MediaVolumeLayout()
        self.add_widget(self.Volume)

        self.pulse = pulsectl.Pulse('karvy')
        self.pulse.event_mask_set('all')
        self.pulse.event_callback_set(self.printPAEvent)
        #self.volume = self.pulse.sink_input_list()[0].volume.value_flat

        self.refreshBTDevice()
        self.triggerRefreshBTDevice = Clock.create_trigger(self.refreshBTDevice)
        self.triggerUpdate = Clock.create_trigger(self.checkUpdate)

        Clock.schedule_interval(self.triggerUpdate, 0.5)

    def on_App_Closing(self):
        #self.transport.Release()
        pass

    def printPAEvent(self, ev):
        pass
        #self.volume = self.pulse.sink_input_list()[0].volume.value_flat

    def refreshBTDevice(self, *args):
        rootBTObj = systembus.get_object('org.bluez', '/')
        managedObjects = rootBTObj.GetManagedObjects(dbus_interface='org.freedesktop.DBus.ObjectManager')

        self.playerObjectPath = None
        self.player = None
        self.transport = None

        #print(managedObjects.items())
        #path:str
        for path in managedObjects:

            #print(path)
            '''
            if "/fd" in path:

                #splittedPath = path.split("/fd")
                                
                self.transportObjectPath = path
                try:
                    self.transport = dbus.Interface(
                            systembus.get_object('org.bluez', self.transportObjectPath),
                            dbus_interface='org.bluez.MediaTransport1',
                    )
                    print(self.transport)
                    print("\n")

                    self.transport_file_descriptor, read_mtu, write_mtu = self.transport.Acquire()
                    print(self.transport_file_descriptor)

                except dbus.exceptions.DBusException as e:
                    print(f"Error initializing MediaTransport interface: {e}")
            '''
            if "/player" in path:
                

                self.playerObjectPath = path
                try:
                    deviceObject = systembus.get_object('org.bluez', self.playerObjectPath[:-8])
                    self.player_name = deviceObject.Get(
                        'org.bluez.Device1',
                        'Alias',
                        dbus_interface='org.freedesktop.DBus.Properties'
                    )

                    self.player = dbus.Interface(
                        systembus.get_object('org.bluez', self.playerObjectPath),
                        dbus_interface='org.bluez.MediaPlayer1',
                    )

                    self.playerPropsDevice = dbus.Interface(
                        systembus.get_object('org.bluez', self.playerObjectPath),
                        dbus_interface='org.freedesktop.DBus.Properties',
                    )

                except dbus.exceptions.DBusException as e:
                    print(f"Error initializing Player interface: {e}")

                    self.checkUpdate()

    def catchDBusErrors(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except dbus.exceptions.DBusException as err:
                
                self.setDefaultValues()
                self.triggerRefreshBTDevice()
        wrapper.__name__ = func.__name__
        return wrapper

    def getPlayer(self):
        systembus.get_object('org.bluez', self.playerObjectPath)

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
        if(self.playerPropsDevice):
            return self.playerPropsDevice and self.playerPropsDevice.Get('org.bluez.MediaPlayer1', name)
        return 0

    def setPlayerProp(self, name, value):
        if(self.playerPropsDevice):
            self.playerPropsDevice and self.playerPropsDevice.Set('org.bluez.MediaPlayer1', name, value)

    def getVolume(self):
        if(self.transport):
            #print(self.transport)
            #return self.transport.Get('org.bluez.MediaTransport1', 'Volume')
            pass
        return 0

    def setVolume(self, value):
        if(self.transport):
            #print(self.transport)
            #self.transport.Set('org.bluez.MediaTransport1', 'Volume', dbus.UInt16(value))
            #self.transport_file_descriptor.Set('org.bluez.MediaTransport1', 'Volume', dbus.UInt16(value))
            pass

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
        
        track = self.getPlayerProp('Track')

        self.duration = int(track['Duration'])
        self.position = int(self.getPlayerProp('Position'))

        self.Time.Slider.range = (0, self.duration)
        self.Time.Slider.value = self.position

        self.Elapsed_Min = (self.position / (1000 * 60)) % 60
        self.Elapsed_Sec = (self.position / 1000) % 60
        self.Left_Min = ((self.duration - self.position) / (1000 * 60)) % 60
        self.Left_Sec = ((self.duration - self.position) / 1000) % 60

        self.Time.Elapsed.text = ("%d:%02d" % (self.Elapsed_Min, self.Elapsed_Sec))
        self.Time.Left.text = ("-%d:%02d" % (self.Left_Min, self.Left_Sec))

        #self.New_Volume = self.getVolume()
        #if(self.New_Volume > 100):
            #self.setVolume(100)
        #self.Volume.Slider.value = self.New_Volume

        self.status = self.getPlayerProp('Status')

        if(self.status == 'playing'):
            self.Control.Play.icon = "pause"
        if(self.status == 'paused'):
            self.Control.Play.icon = "play"

        self.artist = track.get('Artist', '-')
        self.album = track.get('Album', '-')
        self.track = track.get('Title', '-')

        self.pulse.event_listen(timeout=0.001)

class MediaTimeLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MediaTimeLayout, self).__init__(**kwargs)
        self.name = "MediaTimeLayout"
        self.orientation = 'horizontal'
        self.size_hint_y = 0.25
        self.Elapsed = MediaTimeElapsed()
        self.add_widget(self.Elapsed)
        self.Slider = MediaTimeSlider()
        self.add_widget(self.Slider)
        self.Left = MediaTimeLeft()
        self.add_widget(self.Left)
           

class MediaTimeSlider(MDSlider):

    def __init__(self, **kwargs):
        
        super(MediaTimeSlider, self).__init__(**kwargs)
        self.name = "MediaTimeSlider"
        self.range = (0, 10)
        self.orientation = 'horizontal'
        self.step = 1
        self.value = 0
        self.show_off = False
        self.hint = False
        self.size_hint_x = 0.5
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

class MediaTimeElapsed(MDLabel):

    def __init__(self, **kwargs):
        
        super(MediaTimeElapsed, self).__init__(**kwargs)
        self.name = "MediaTimeElapsed"
        self.text = "0:00"
        self.font_style = 'H4'
        self.size_hint_x = 0.25
        self.halign = 'center'

class MediaTimeLeft(MDLabel):

    def __init__(self, **kwargs):
        
        super(MediaTimeLeft, self).__init__(**kwargs)
        self.name = "MediaTimeLeft"
        self.text = "-0:00"
        self.font_style = 'H4'
        self.size_hint_x = 0.25
        self.halign = 'center'

class MediaControlLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MediaControlLayout, self).__init__(**kwargs)
        self.name = "MediaControlLayout"
        self.orientation = 'horizontal'
        self.size_hint_y = 0.5
        self.spacing = "100dp"
        self.Back = MediaBackButton()
        self.add_widget(self.Back)
        self.Play = MediaPlayButton()
        self.add_widget(self.Play)
        self.Next = MediaNextButton()
        self.add_widget(self.Next)

class MediaPlayButton(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaPlayButton, self).__init__(**kwargs)
        self.name = "MediaPlayButton"
        self.size_hint = (0.3,0.3) 
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.on_press = self.Pressed
        self.icon = "play"
        self.icon_size = "75dp"
        self.start = time.time()

    def Pressed(self):
        self.end = time.time()

        if((self.end - self.start) > 0.5):

            self.start = time.time()
            Debug.Start("MediaPlayButton -> Pressed")

            if self.icon == "pause":
                Debug.Log("Was pause, is now play")
                self.icon = "play"
                self.parent.parent.pause()
            elif self.icon == "play":
                Debug.Log("Was play, is now pause")
                self.icon = "pause"
                self.parent.parent.play()
            Debug.End()

class MediaNextButton(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaNextButton, self).__init__(**kwargs)
        self.name = "MediaNextButton"
        self.icon = "skip-next"
        self.icon_size = "75dp"
        self.size_hint = (0.3,0.3) 
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.NextPressed = False
        self.on_press = self.Pressed
        self.start = time.time()

    def Pressed(self):
        self.end = time.time()

        if((self.end - self.start) > 0.5):

            self.start = time.time()
            Debug.Start("MediaNextButton -> Pressed")

            self.parent.parent.next()

            Debug.End()

class MediaBackButton(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaBackButton, self).__init__(**kwargs)
        self.name = "MediaBackButton"
        self.icon = "skip-previous"
        self.icon_size = "75dp"
        self.size_hint = (0.3,0.3) 
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.BackPressed = False
        self.on_press = self.Pressed
        self.start = time.time()

    def Pressed(self):
        self.end = time.time()

        if((self.end - self.start) > 0.5):

            self.start = time.time()
            Debug.Start("MediaBackButton -> Pressed")

            self.parent.parent.previous()

            Debug.End()

class MediaVolumeLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        
        super(MediaVolumeLayout, self).__init__(**kwargs)
        self.name = "MediaControlLayout"
        self.orientation = 'horizontal'
        self.size_hint_y = 0.25
        self.IconDown = MediaVolumeDownIcon()
        self.add_widget(self.IconDown)
        self.Slider = MediaVolumeSlider()
        self.add_widget(self.Slider)
        self.IconUp = MediaVolumeUpIcon()
        self.add_widget(self.IconUp)
        self.Volume = 25

class MediaVolumeSlider(MDSlider):

    def __init__(self, **kwargs):
        
        super(MediaVolumeSlider, self).__init__(**kwargs)
        self.name = "MediaVolumeSlider"
        self.range = (0, 255)
        self.orientation = 'horizontal'
        self.step = 5
        self.value = 10
        self.hint = True
        self.size_hint_x = 0.5
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.bind(value = self.changed_value)

    def changed_value(self, *args):
        self.parent.parent.setVolume(self.value)

class MediaVolumeUpIcon(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaVolumeUpIcon, self).__init__(**kwargs)
        self.name = "MediaVolumeUpIcon"
        self.icon = "volume-high"
        self.icon_size = "50dp"
        self.size_hint_x = 0.25
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.on_press = self.Pressed
        self.start = time.time()

    def Pressed(self):
        self.end = time.time()

        if((self.end - self.start) > 0.5):

            self.start = time.time()
            Debug.Start("MediaVolumeUp -> Pressed")
            self.NewVolume = self.parent.parent.getVolume() + 5
            if(self.NewVolume <= 100):
                self.parent.parent.setVolume(self.NewVolume)

            Debug.End()

class MediaVolumeDownIcon(MDIconButton):

    def __init__(self, **kwargs):
        
        super(MediaVolumeDownIcon, self).__init__(**kwargs)
        self.name = "MediaVolumeDownIcon"
        self.icon = "volume-medium"
        self.icon_size = "50dp"
        self.size_hint_x = 0.25
        self.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.on_press = self.Pressed
        self.start = time.time()

    def Pressed(self):
        self.end = time.time()

        if((self.end - self.start) > 0.5):

            self.start = time.time()
            Debug.Start("MediaVolumeDown -> Pressed")

            self.NewVolume = self.parent.parent.getVolume() - 5
            if(self.NewVolume >= 0):
                self.parent.parent.setVolume(self.NewVolume)

            Debug.End()