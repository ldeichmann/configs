#!/bin/bash

bspc query -N -n .leaf.fullscreen
RET=$?
if [ $RET -ne 0 ] ; then
    echo locking
    $(realpath ~/.config/bspwm/scripts/lock.sh)
fi
