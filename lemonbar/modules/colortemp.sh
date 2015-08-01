echo -n "" > /tmp/lemon/colortemp.out
while true; do
	TEMP=$(redshift -p | grep K | sed 's/.*: //')
	CLICK="%{A1:pkill -USR1 redshift &:}"
	FULL=$CLICK" $TEMP""%{A}"
	#sed -i "11 c\\$FULL" ~/.config/lemonbar/bar.out
	
	CONTENT=$(cat /tmp/lemon/colortemp.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > /tmp/lemon/colortemp.out
	fi
	#echo -n "$FULL" > /tmp/lemon/colortemp.out

	sleep 10;
done