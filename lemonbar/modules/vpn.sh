echo -n "" > /tmp/lemon/vpn.out
while true; do
	CLICK="%{A1:urxvt -e nmtui &:}"
	ps -aux | grep openvpn | grep -v 'grep' | grep -v 'sed' > /dev/null
	if [ $? -eq 1 ]; then
		FULL=$CLICK"%{F#ffff6961}""""%{F#ffffffff}""%{A}"
	else
		VPN=$(ps -aux | grep openvpn | grep -v 'grep openvpn' | egrep -o '\-\-remote [a-z\.]+' | sed 's/--remote //g')
		FULL=$CLICK" $VPN""%{A}"
	fi
	#sed -i "12 c\\$FULL" ~/.config/lemonbar/bar.out
	
	CONTENT=$(cat /tmp/lemon/vpn.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > /tmp/lemon/vpn.out
	fi

	sleep 10;
done