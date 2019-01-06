#!/usr/bin/env python3

# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import sys

# Bizbot Sesehat
from sense_hat import SenseHat
sense = SenseHat()

#set GPIO numbering mode and define output pins
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)
#GPIO.setup(13,GPIO.OUT)
#GPIO.setup(15,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                #GPIO.output(7,False)
                #print ("UP")
                sense.show_message("UP")
            elif char == curses.KEY_DOWN:
                #GPIO.output(7,True)
                #print ("DOWN")
                sense.show_message("DOWN")
            elif char == curses.KEY_RIGHT:
                #GPIO.output(7,True)
                #print ("RIGHT")
                sense.show_message("RIGHT")
            elif char == curses.KEY_LEFT:
                #GPIO.output(7,False)
                #print ("LEFT")
                sense.show_message("LEFT")
            elif char == 10:
                #GPIO.output(7,False)
                #print ("10")
                sense.show_message("ENTER")

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
