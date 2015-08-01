echo -n "" > /tmp/lemon/ssid.out
while true; do
	SSID=$(iwgetid -r)
	CLICK="%{A1:urxvt -e nmtui &:}"
	FULL=$CLICK"SSID: $SSID""%{A}"
	#echo -n $CLICK"SSID: $SSID""%{A}"
	CONTENT=$(cat /tmp/lemon/ssid.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > /tmp/lemon/ssid.out
	fi

	#echo -n "$FULL" > /tmp/lemon/ssid.out
done