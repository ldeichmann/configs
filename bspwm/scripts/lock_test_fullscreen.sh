#!/bin/bash

bspc query -N -n .leaf.fullscreen
RET=$?
if [ $RET -ne 0 ] ; then
    echo locking
    LINK=$(readlink -f $0)
    DIR=$(dirname $LINK)
    $DIR/lock.sh
fi
