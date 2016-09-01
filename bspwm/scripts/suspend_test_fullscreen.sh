#!/bin/bash

status=$(mpc status)
pgrep pacaur
pacaur_running=$?

#if pacaur isn't running and mpd is not playing a track, suspend...
if [[ $status != *"[playing]"* ]] && [ $pacaur_running -ne 0 ]; then
    echo suspending
    systemctl suspend
fi
