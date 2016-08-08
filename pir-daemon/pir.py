#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess

ScreenTimeout = 60
MonitorTimeout = 600

Counter = MonitorTimeout
Screen = True
Monitor = True

GPIO_PIR = 24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def reset_counter(channel):
  global ScreenTimeout,MonitorTimeout, Counter, Screen, Monitor
  Counter = MonitorTimeout
  if not Monitor:
    Monitor = True
    subprocess.call('/usr/bin/tvservice -p', shell=True)                                                                                                                          
    #print "Monitor aan"                                                                                                                                                          
  if not Screen:                                                                                                                                                                  
    Screen = True                                                                                                                                                                 
    subprocess.call('/usr/bin/xset dpms force on', shell=True)                                                                                                                    
    #print "Screen aan"                                                                                                                                                           
                                                                                                                                                                                  
GPIO.add_event_detect(GPIO_PIR, GPIO.RISING, callback=reset_counter)                                                                                                              

# Disable DPMS, only turn monitor on/off
#subprocess.call('/usr/bin/xset -dpms', shell=True)
subprocess.call('/usr/bin/xset dpms force on', shell=True)

try:
  while True:
      #print "Tick " + str(Counter)
      if Counter:
        Counter -= 1
      if Counter < MonitorTimeout - ScreenTimeout and Screen:
        subprocess.call('/usr/bin/xset dpms force off', shell=True)
        Screen = False
        #print "Screen uit"
      if not Counter and Monitor:
        subprocess.call('/usr/bin/tvservice -o', shell=True)
        Monitor = False
        #print "Monitor uit"
      time.sleep(1)
except KeyboardInterrupt:
    print "Quit"

GPIO.cleanup()

