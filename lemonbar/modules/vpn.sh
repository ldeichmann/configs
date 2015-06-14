ps -aux | grep openvpn | grep -v 'grep' | grep -v 'sed' > /dev/null
if [ $? -eq 1 ]; then
	echo -n "%{F#ffff6961}""""%{F#ffffffff}"
else
	VPN=$(ps -aux | grep openvpn | grep -v 'grep openvpn' | egrep -o '\-\-remote [a-z\.]+' | sed 's/--remote //g')
	echo -n " $VPN"
fi