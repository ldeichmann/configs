#!/bin/bash

# i3lock blurred screen inspired by /u/patopop007 and the blog post
# http://plankenau.com/blog/post-10/gaussianlock

# Dependencies:
# imagemagick
# i3lock
# scrot (optional but default)

IMAGE=/tmp/i3lock.png
SCREENSHOT="scrot $IMAGE"

# Get the screenshot, add the blur and lock the screen with it
$SCREENSHOT
convert -filter Gaussian -resize 20% -define filter:sigma=1.5 -resize 500.5% -set colorspace Gray -separate -average $IMAGE $IMAGE
i3lock -n -i $IMAGE
rm $IMAGE
