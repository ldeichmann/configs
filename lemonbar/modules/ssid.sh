SSID=$(netctl-auto list | grep \* | sed 's/.*s0-//')
echo -n "SSID: $SSID"