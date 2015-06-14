TEMP=$(redshift -p -l 0:0 | grep K | sed 's/.*: //')
echo -n " $TEMP"