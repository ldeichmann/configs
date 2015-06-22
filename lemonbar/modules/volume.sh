OPENPAVU="%{A3:pavucontrol &:}"
VOLUP="%{A4:pamixer --increase 5:}"
VOLDOWN="%{A5:pamixer --decrease 5:}"
MUTE="%{A1:pamixer --toggle-mute:}"
ISMUTE=$(pamixer --get-mute)
VOL=$(pamixer --get-volume)
if [ $ISMUTE = true ]; then
	echo -n "$MUTE""%{F#ffff6961}""   $VOL%""%{F#ffffffff}""%{A}"
else
	echo -n "$MUTE""$OPENPAVU""$VOLDOWN""$VOLUP"" $VOL%""%{A}%{A}%{A}%{A}"
fi
