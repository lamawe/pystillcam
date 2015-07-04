#!/usr/bin/env python2.7
#

import sys
import time
import RPi.GPIO as GPIO

# Action when shutter is pressed
def shutter_pressed(channel):
    print "Shutter Pressed! "  + str(channel)

# Before Main Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17, GPIO.FALLING, callback=shutter_pressed, bouncetime=300) 


def main(argv):
    print GPIO.VERSION

    i = 0
    while True:
        time.sleep(0.2)
        if ((i % 25) == 0):
            input_state = GPIO.input(17)
            print i
            print input_state
            print 
        i += 1



if __name__ == "__main__":
    main(sys.argv)



'''
    while True:
        input_state = GPIO.input(17)
        if input_state == False:
            print('Button Pressed')
            time.sleep(0.2)
'''

