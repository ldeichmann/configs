TEMP=$(redshift -p | grep K | sed 's/.*: //')
echo -n " $TEMP"
