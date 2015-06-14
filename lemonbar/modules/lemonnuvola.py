#!/usr/bin/env python3
"""
Display the current "artist - title" playing in nuvola.

@author Francois LASSERRE <choiz@me.com>
@license GNU GPL http://www.gnu.org/licenses/gpl.html
"""

from time import time
from subprocess import check_output, call


def buildString():
    try:
        metadatas = check_output("qdbus-qt4 org.mpris.MediaPlayer2.NuvolaPlayer3GooglePlayMusic /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player Metadata", shell=True)
        playbackstatus = check_output("qdbus-qt4 org.mpris.MediaPlayer2.NuvolaPlayer3GooglePlayMusic /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player PlaybackStatus", shell=True)
        cmd = "qdbus-qt4 org.mpris.MediaPlayer2.NuvolaPlayer3GooglePlayMusic /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player."
        lines = metadatas.decode('utf-8').split('\n')
        lines = filter(None, lines)
        isplaying = playbackstatus.decode('utf-8').split('\n')

        now_playing = ''
        playbackicon = ''
        
        if "Playing" in isplaying:
            playbackicon = ''
        elif "Paused" in isplaying:
            playbackicon = ''
        elif "Stopped" in isplaying:
            playbackicon = ''


        if lines:
            artist = ''
            title = ''

            for item in lines:
                if item.find('xesam:artist:') != -1:
                    artist = item[14:]
                if item.find('xesam:title:') != -1:
                    title = item[13:]

            if artist and title:
                now_playing = '{} - {}'.format(artist, title)
            elif artist:
                now_playing = '{}'.format(artist)
            elif title:
                now_playing = '{}'.format(title)
            if artist or title:
                now_playing = playbackicon + " %{A1:"+cmd+"PlayPause"+":}" \
                + "%{A2:"+cmd+"Previous"+":}" \
                + "%{A3:"+cmd+"Next"+":}" \
                + "%{F#ffffffff}" + now_playing \
                + "%{A}%{A}%{A}"
        else:
            now_playing = ''

        return now_playing

    except:
        return ''



if __name__ == "__main__":
    print(buildString())