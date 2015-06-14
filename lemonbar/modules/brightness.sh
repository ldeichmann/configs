BRIGHT=$(xbacklight | awk '{printf("%1.f\n", $1)}')
echo -n "Brightness: $BRIGHT%"