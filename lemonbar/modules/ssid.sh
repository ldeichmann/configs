SSID=$(iwgetid -r)
CLICK="%{A1:urxvt -e nmtui &:}"
echo -n $CLICK"SSID: $SSID""%{A}"
