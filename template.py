#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Songeziwe S. Soboois
Student Number: SBSSON002
Prac: Prac 0
Date: 23/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep

# List of pins used from the RPI:
# Pin 6 - Ground
# Pin 7 - LED0
# Pin 12- LED1
# Pin 11- LED2
# Pin 13- Black button
# Pin 15- Red button

# Global variables
LEDS    = (7, 12, 11)
BUTTONS = (13, 15)

# Function for initializing the PI
def init_GPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LEDS, GPIO.OUT)
    # have to setup the buttons

def light_LED():
    GPIO.output(LEDS, GPIO.HIGH)
    sleep(1)
    GPIO.output(LEDS, GPIO.LOW)
    sleep(1)

def main():
    light_LED()

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    init_GPIO()
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
