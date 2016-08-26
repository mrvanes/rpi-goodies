# pir-daemon
PIR element used: [AMN31112J PIR-bewegingssensor](https://www.conrad.nl/nl/panasonic-amn31112j-pir-bewegingssensor-amn3-soort-behuizing-vingerhoed-behuizing-3-6-v-504928.html)

I needed to add a 10k pull-down resistor between OUT (signal) and GND to reliably detect movement.

Make sure to run the daemon as user that owns the X11 session by starting it from the Window Manager autostart configuration, otherwise the $DISPLAY environment won't be correct. 
