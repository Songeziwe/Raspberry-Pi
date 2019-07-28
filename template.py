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
    GPIO.add_event_detect(BUTTONS[0], GPIO.RISING, light_LED)
# Function for blinking LEDs
def light_LED(event):
    GPIO.output(LEDS, [1, 1, 1])
    sleep(0.1)
    GPIO.output(LEDS, [0, 0, 0])

def main():
    #GPIO.add_event_detect(BUTTONS[0], GPIO.RISING, light_LED)
    a = 0
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
