BRIGHT=$(xbacklight | awk '{printf("%1.f\n", $1)}')
BUP="%{A4:xbacklight -inc 10:}"
BDOWN="%{A5:xbacklight -dec 10:}"
echo -n "$BUP""$BDOWN""Brightness: $BRIGHT%""%{A}%{A}"