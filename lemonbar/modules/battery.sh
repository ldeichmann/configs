echo -n "" > /tmp/lemon/battery.out
while true; do

	BAT=$(acpi -b | cut -d, -f2 | sed 's/ //g')
	FULL="Battery: $BAT"
	#echo -n "Battery: $BAT"
	#sed -i "8 c\\$BAT/" ~/.config/lemonbar/bar.out
	
	CONTENT=$(cat /tmp/lemon/vpn.out)

	if [ "$CONTENT" != "FULL" ]; then
		echo -n "$FULL" > /tmp/lemon/battery.out
	fi
	#echo -n "Battery: $BAT" > /tmp/lemon/battery.out
	
	sleep 10;

done
