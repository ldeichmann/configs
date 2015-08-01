echo -n "" > ~/.config/lemonbar/modules/ssid.out
while true; do
	SSID=$(iwgetid -r)
	CLICK="%{A1:urxvt -e nmtui &:}"
	FULL=$CLICK"SSID: $SSID""%{A}"
	#echo -n $CLICK"SSID: $SSID""%{A}"
	CONTENT=$(cat ~/.config/lemonbar/modules/ssid.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > ~/.config/lemonbar/modules/ssid.out
	fi

	#echo -n "$FULL" > ~/.config/lemonbar/modules/ssid.out
done