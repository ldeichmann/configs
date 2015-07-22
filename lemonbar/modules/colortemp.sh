TEMP=$(redshift -p | grep K | sed 's/.*: //')
CLICK="%{A1:pkill -USR1 redshift &:}"
echo -n $CLICK" $TEMP""%{A}"
