import os
import time
import subprocess
import pydbus
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class BluetoothSpeaker:
    def __init__(self):
        self.player = None
        self.last_device_address = None

    def enable_discoverability(self):
        subprocess.run(["sudo", "hciconfig", "hci0", "piscan"])

    def accept_connections(self):
        bus = pydbus.SystemBus()
        manager = bus.get('org.bluez', '/org/bluez')
        manager.RegisterAgent('/org/bluez/Agent', 'NoInputNoOutput')
        manager.RequestDefaultAgent('/org/bluez/Agent')

        adapter_path = manager.DefaultAdapter()
        adapter = bus.get('org.bluez', adapter_path)
        adapter.StartDiscovery()

        Gtk.main()

    def on_device_connected(self, device_path):
        bus = pydbus.SystemBus()
        device = bus.get('org.bluez', device_path)

        if device.Address == self.last_device_address:
            self.connect_to_device(device)
        else:
            pass
            # New device connected, prompt user for connection
            # You can use your KivyMD interface here to prompt the user

    def connect_to_device(self, device):
        self.last_device_address = device.Address

        bus = pydbus.SystemBus()
        player = bus.get('org.bluez', device.object_path).MediaControl1
        player.Connect()

        self.player = player

    def stream_audio_to_audio_jack(self):
        # Redirect audio to audio jack using amixer
        subprocess.run(["amixer", "cset", "numid=3", "1"])

    def execute_avcrp_command(self, command):
        if self.player:
            if command == 'play_pause':
                self.player.PlayPause()
            elif command == 'next_track':
                self.player.Next()
            elif command == 'previous_track':
                self.player.Previous()
            elif command.startswith('volume_'):
                volume = int(command.split('_')[1])
                self.player.Volume(volume)

    def reconnect_last_device(self):
        if self.last_device_address:
            self.connect_to_device(self.last_device_address)

if __name__ == '__main__':
    speaker = BluetoothSpeaker()
    speaker.enable_discoverability()
    speaker.accept_connections()
    speaker.stream_audio_to_audio_jack()
