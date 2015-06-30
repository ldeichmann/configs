#!/bin/bash
VAL=500
if [[ $(nvidia-settings -q "[gpu:0]/DigitalVibrance[DFP-0]" | grep "Attribute.*$VAL\.") ]]
then
	nvidia-settings -a "[gpu:0]/DigitalVibrance[DFP-0]=0" > /dev/null
	echo "Vibrance Disabled"
else
	nvidia-settings -a "[gpu:0]/DigitalVibrance[DFP-0]=$VAL" > /dev/null
	echo "Vibrance Enabled"
fi
