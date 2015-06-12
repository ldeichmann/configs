# -*- coding: utf-8 -*-
"""
Display the current "artist - title" playing in nuvola.

@author Francois LASSERRE <choiz@me.com>
@license GNU GPL http://www.gnu.org/licenses/gpl.html
"""

from time import time
from subprocess import check_output, call


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 5

    def _sendEvent(self, event):

        cmd = "qdbus-qt4 org.mpris.MediaPlayer2.NuvolaPlayer3GooglePlayMusic /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player." + event

        try:
            call(cmd, shell=True)
        except:
            pass

    def on_click(self, i3s_output_list, i3s_config, event):
        """
        This method should only be used for ADVANCED and very specific usages.
        Read the 'Handle click events directly from your i3status config'
        article from the py3status wiki:
            https://github.com/ultrabug/py3status/wiki/
        This method will be called when a click event occurs on this module's
        output on the i3bar.
        Example 'event' json object:
        {'y': 13, 'x': 17, 'button': 1, 'name': 'example', 'instance': 'first'}
        """
        if event['button'] == 1:
            self._sendEvent("PlayPause")
        elif event['button'] == 2:
            self._sendEvent("Previous")
        elif event['button'] == 3:
            self._sendEvent("Next")
        else:
            print(event['button'])


    def _getMetadatas(self):
        """
        Get the current song metadatas (artist - title)
        NuvolaPlayer3GooglePlayMusic
        """
        try:
            metadatas = check_output("qdbus-qt4 org.mpris.MediaPlayer2.NuvolaPlayer3GooglePlayMusic /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player Metadata", shell=True)
            lines = metadatas.decode('utf-8').split('\n')
            lines = filter(None, lines)

            now_playing = ''

            if lines:
                artist = ''
                title = ''

                for item in lines:
                    if item.find('xesam:artist:') != -1:
                        artist = item[14:]
                    if item.find('xesam:title:') != -1:
                        title = item[13:]

                if artist and title:
                    now_playing = '♫ {} - {}'.format(artist, title)
                elif artist:
                    now_playing = '♫ {}'.format(artist)
                elif title:
                    now_playing = '♫ {}'.format(title)
            else:
                now_playing = ''

            return now_playing
        except:
            return ''

    def nuvola(self, i3s_output_list, i3s_config):
        """
        Get the current "artist - title" and return it.
        """
        response = {'full_text': ''}

        response['cached_until'] = time() + self.cache_timeout
        response['full_text'] = self._getMetadatas()

        return response

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    """
    from time import sleep
    x = Py3status()
    config = {
        'color_good': '#00FF00',
        'color_bad': '#FF0000',
    }
    while True:
        print(x.nuvola([], config))
        sleep(1)