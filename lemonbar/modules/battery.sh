echo -n "" > ~/.config/lemonbar/modules/battery.out
while true; do

	BAT=$(acpi -b | cut -d, -f2 | sed 's/ //g')
	FULL="Battery: $BAT"
	#echo -n "Battery: $BAT"
	#sed -i "8 c\\$BAT/" ~/.config/lemonbar/bar.out
	
	CONTENT=$(cat ~/.config/lemonbar/modules/vpn.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > ~/.config/lemonbar/modules/battery.out
	fi
	#echo -n "Battery: $BAT" > ~/.config/lemonbar/modules/battery.out
	
	sleep 10;

done
