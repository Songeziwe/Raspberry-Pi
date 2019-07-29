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
# Pin 13- LED1
# Pin 15- LED2
# Pin 11- Black button : increment
# Pin 12- Red button   : decrement

# Global variables
LEDS    = (7, 13, 15)
BUTTONS = (11, 12)
counter = 0

# Function for initializing the PI
def init_GPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LEDS[0], GPIO.OUT)
    GPIO.setup(LEDS[1], GPIO.OUT)
    GPIO.setup(LEDS[2], GPIO.OUT)

    GPIO.setup(BUTTONS[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTONS[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Ensure that all LEDs are off initially
    GPIO.output(LEDS, [0, 0, 0])
    GPIO.add_event_detect(BUTTONS[0], GPIO.RISING, callback=increment, bouncetime=300)
    GPIO.add_event_detect(BUTTONS[1], GPIO.RISING, callback=decrement, bouncetime=300)

# Increment the counter
# This method will be executed when an interrupt occures
# event - pin number of the clicked button
def increment(event):
    global counter
    counter += 1
    if counter > 7:
        counter = 0

# Decrement the counter
# This Function will be executed when an interrupt occures
# event - pin number of the clicked button
def decrement(event):
    global counter
    counter -= 1
    if counter < 0:
        counter = 7

# convert counter to Binary
# value  - number to be converted to binary
# return - a list of 0's and/or 1's representing the value 
def convert2Binary(value):
    binaryList = []
    result = value
    while True:
        remainder = result % 2
        result = result // 2
        if remainder == 0:
            binaryList.append(0)
        else:
            binaryList.append(1)

        if result <= 0:
            break
    if len(binaryList) < 2:
        binaryList.append(0)
        binaryList.append(0)
    elif len(binaryList) < 3:
        binaryList.append(0)
    return binaryList

# Function for blinking LEDs
def light_LED():
    binary = convert2Binary(counter)
    GPIO.output(LEDS, binary)

def main():
   light_LED()
 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    GPIO.setwarnings(False)
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
