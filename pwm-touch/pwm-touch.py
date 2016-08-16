#!/usr/bin/python
from evdev import InputDevice, categorize, ecodes
from select import select
import wiringpi as wp

dev = InputDevice('/dev/input/touchscreen')

wp.wiringPiSetupGpio()
wp.pinMode(18,wp.PWM_OUTPUT)
wp.pwmSetClock(20000)
wp.pwmSetRange(100)
wp.pwmWrite(18,50)

while True:
  # Lighweight wait for IO activity on device
  select([dev], [], [])
  
  for event in dev.read():
    if event.type == ecodes.EV_ABS
      # PiTFT 2.8 capacitive reports ABS_MT_POSITION_Y events
      if event.code == ecodes.ABS_MT_POSITION_Y:
        # PiTFT 2.8 capacitive events range from exactly 0 to 320
        dc = 100*(320-event.value)/320

      # PiTFT 2.8 resistive reports ABS_Y events
      #if event.code == ecodes.ABS_Y:
        # PiTFT 2.8 resistive Y events range from approx. 700 to 3900
        #dc = 100*(event.value-700)/3200

        # Debug events, you should also try evtest /dev/input/[device] for proper eventnames
        #print(dc)
        wp.pwmWrite(18,dc)
