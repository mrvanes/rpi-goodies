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
  select([dev], [], [])
  for event in dev.read():
    if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_MT_POSITION_Y:
      dc = 100*(320-event.value)/320
      #print(dc)
      wp.pwmWrite(18,dc)
