#!/usr/bin/env python3
"""
Display the current "artist - title" playing in nuvola.

@author Francois LASSERRE <choiz@me.com>
@license GNU GPL http://www.gnu.org/licenses/gpl.html
"""

from gi.repository import Playerctl

def buildString():
#    playername = 'NuvolaPlayer3GooglePlayMusic'
    playername = 'gme'
    cmd = 'playerctl --player=' + playername + ' '
    playercmdprev = "%{A2:"+cmd+"previous &:}"
    playercmdnext = "%{A3:"+cmd+"next &:}"
    playercmdpause = "%{A1:"+cmd+"play-pause &:}"
    try:
	    player = Playerctl.Player(player_name=playername)
	    playerstatus = player.props.status

	    if playerstatus is None:
	        return ''

	    playbackicon = ''
	    
	    if "Playing" == playerstatus:
	        playbackicon = ' '
	    elif "Paused" == playerstatus:
	        playbackicon = ' '
	    elif "Stopped" == playerstatus:
	        playbackicon = ' '

	    artist = player.get_artist()
	    title = player.get_title()

	    if artist and title:
	        return playbackicon + playercmdpause \
	            +  playercmdprev + playercmdnext \
	            + "%{F#ffffffff}" + artist \
	            + ' - ' + title + "%{A}%{A}%{A}"


    except:
        return 'Except'



if __name__ == "__main__":
    print(buildString())
