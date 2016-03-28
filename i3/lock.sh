#!/bin/bash

# i3lock blurred screen inspired by /u/patopop007 and the blog post
# http://plankenau.com/blog/post-10/gaussianlock

# Timings are on an Intel i7-2630QM @ 2.00GHz

# Dependencies:
# imagemagick
# i3lock
# scrot (optional but default)

IMAGE=/tmp/i3lock.png
SCREENSHOT="scrot $IMAGE" # 0.46s

# Get the screenshot, add the blur and lock the screen with it
$SCREENSHOT
#convert -scale 10% -scale 1000% $IMAGE $IMAGE
convert -filter Gaussian -resize 20% -define filter:sigma=1.5 -resize 500.5% -set colorspace Gray -separate -average $IMAGE $IMAGE
sleep 5
i3lock -i $IMAGE
sleep 5
rm $IMAGE
