BAT=$(acpi -b | cut -d, -f2 | sed 's/ //g')
echo -n "Battery: $BAT"