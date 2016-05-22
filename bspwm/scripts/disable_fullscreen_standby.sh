#!/bin/bash

bspc subscribe node_state | grep --line-buffered "fullscreen" | while read -r _; do
    bspc query -N -n .leaf.fullscreen > /dev/null 2>&1
    RET=$?
    if [ $RET -eq 0 ] ; then
        echo "disable standby"
        xset -dpms
    else
        echo "enable standby"
        xset +dpms
    fi
done
