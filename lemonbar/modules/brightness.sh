echo -n "" > ~/.config/lemonbar/modules/brightness.out
while true; do
	BRIGHT=$(xbacklight | awk '{printf("%1.f\n", $1)}')
	BUP="%{A4:xbacklight -inc 10:}"
	BDOWN="%{A5:xbacklight -dec 10:}"
	FULL="$BUP""$BDOWN""Brightness: $BRIGHT%""%{A}%{A}"
	#echo -n "$BUP""$BDOWN""Brightness: $BRIGHT%""%{A}%{A}"
	#sed -i "7 c\\FULL" ~/.config/lemonbar/bar.out
		
	CONTENT=$(cat ~/.config/lemonbar/modules/brightness.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > ~/.config/lemonbar/modules/brightness.out
	fi
	#echo -n "$FULL" > ~/.config/lemonbar/modules/brightness.out

	sleep 1;
done