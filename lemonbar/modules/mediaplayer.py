#!/usr/bin/env python3
"""
Display the current "artist - title" playing in nuvola.

@author Francois LASSERRE <choiz@me.com>
@license GNU GPL http://www.gnu.org/licenses/gpl.html
"""

from gi.repository import Playerctl
from os.path import expanduser
import dbus
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop
from dbus.exceptions import DBusException

class GMENotifier(object):

    def __init__(self):
        """initialise."""
        bus_loop = DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SessionBus(mainloop=bus_loop)
        loop = GObject.MainLoop()
        f = open('/tmp/lemon/mediaplayer.out', 'w')
        print("", file=f, end="")
        try: 
            self.props_changed_listener()
        except DBusException as e:
            if not ("org.mpris.MediaPlayer2.google-music-electron "
                    "was not provided") in e.get_dbus_message():
                raise
        self.session_bus = self.bus.get_object("org.freedesktop.DBus", 
                                 "/org/freedesktop/DBus")
        self.session_bus.connect_to_signal("NameOwnerChanged", 
                                        self.handle_name_owner_changed,
                                        arg0="org.mpris.MediaPlayer2.google-music-electron")

        loop.run()

    def props_changed_listener(self):
        """Hook up callback to PropertiesChanged event."""
        self.googlemusicelectron = self.bus.get_object("org.mpris.MediaPlayer2.google-music-electron", 
                                           "/org/mpris/MediaPlayer2")
        self.googlemusicelectron.connect_to_signal("PropertiesChanged", 
                                        self.handle_properties_changed)
        f = open('/tmp/lemon/mediaplayer.out', 'w')
        print(self.buildString(), file=f, end="")

    def handle_name_owner_changed(self, name, older_owner, new_owner):
        """Introspect the NameOwnerChanged signal to work out if GME has started."""
        if name == "org.mpris.MediaPlayer2.google-music-electron":
            if new_owner:
                # GME has been launched - hook it up.
                self.props_changed_listener()
            else:
                self.googlemusicelectron = None
                f = open('/tmp/lemon/mediaplayer.out', 'w')
                print("", file=f, end="")


    def handle_properties_changed(self, interface, changed_props, invalidated_props):
        """Handle track changes."""
        f = open('/tmp/lemon/mediaplayer.out', 'w')
        print(self.buildString(), file=f, end="")

    def buildString(self):
    #    playername = 'NuvolaPlayer3GooglePlayMusic'
        playername = 'google-music-electron'
        cmd = 'playerctl --player=' + playername + ' '
        playercmdprev = "%{A2:"+cmd+"previous &:}"
        playercmdnext = "%{A3:"+cmd+"next &:}"
        playercmdpause = "%{A1:"+cmd+"play-pause &:}"
        try:
            player = Playerctl.Player(player_name=playername)
            playerstatus = player.props.status

            if playerstatus is None or playerstatus is 'None':
                return ''

            playbackicon = ''
            
            if "Playing" == playerstatus:
                playbackicon = '|  '
            elif "Paused" == playerstatus:
                playbackicon = '|  '
            elif "Stopped" == playerstatus:
                playbackicon = '|  '

            artist = player.get_artist()
            title = player.get_title()

            if artist and title:
                return playbackicon + playercmdpause \
                    +  playercmdprev + playercmdnext \
                    + "%{F#ffffffff}" + artist \
                    + ' - ' + title + "%{A}%{A}%{A}"
            else:
            	return '| Not Playing'


        except:
            return 'Except'

if __name__ == "__main__":
    GMENotifier()