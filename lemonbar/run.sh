#!/bin/bash
killall lemonbar
~/.config/lemonbar/lemonbar_new HDMI-0 | lemonbar -f "Droid Sans-9" -f "FontAwesome" -B "#00000000" -F "#FFFFFFFF" -g 1920x16+0+0 | bash &
~/.config/lemonbar/lemonbar_new DVI-I-1 | lemonbar -f "Droid Sans" -f "FontAwesome" -B "#00000000" -F "#FFFFFFFF" -g 2560x20+1920+0 | bash &
#~/.config/lemonbar/lemonbar | lemonbar -f "Droid Sans-9" -f "FontAwesome" -B "#00000000" -F "#FFFFFFFF" -g 1920x16+0+0 | bash &
#~/.config/lemonbar/lemonbar2 | lemonbar -f "Droid Sans" -f "FontAwesome" -B "#00000000" -F "#FFFFFFFF" -g 2560x20+1920+0 | bash &
