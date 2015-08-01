echo -n "" > /tmp/lemon/volume.out
while true; do
	OPENPAVU="%{A3:pavucontrol &:}"
	VOLUP="%{A4:pamixer --increase 5:}"
	VOLDOWN="%{A5:pamixer --decrease 5:}"
	MUTE="%{A1:pamixer --toggle-mute:}"
	ISMUTE=$(pamixer --get-mute)
	VOL=$(pamixer --get-volume)
	if [ $ISMUTE = true ]; then
		FULL="$MUTE""%{F#ffff6961}""   $VOL%""%{F#ffffffff}""%{A}"
	else
		FULL="$MUTE""$OPENPAVU""$VOLDOWN""$VOLUP"" $VOL%""%{A}%{A}%{A}%{A}"
	fi
	#sed -i "10 c\\$FULL" ~/.config/lemonbar/bar.out

	CONTENT=$(cat /tmp/lemon/volume.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > /tmp/lemon/volume.out
	fi
	#echo -n "$FULL" > /tmp/lemon/volume.out
	sleep 0.5;
done