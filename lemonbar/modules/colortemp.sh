echo -n "" > ~/.config/lemonbar/modules/colortemp.out
while true; do
	TEMP=$(redshift -p | grep K | sed 's/.*: //')
	CLICK="%{A1:pkill -USR1 redshift &:}"
	FULL=$CLICK" $TEMP""%{A}"
	#sed -i "11 c\\$FULL" ~/.config/lemonbar/bar.out
	
	CONTENT=$(cat ~/.config/lemonbar/modules/colortemp.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > ~/.config/lemonbar/modules/colortemp.out
	fi
	#echo -n "$FULL" > ~/.config/lemonbar/modules/colortemp.out

	sleep 10;
done