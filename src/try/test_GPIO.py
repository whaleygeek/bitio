# WORK IN PROGRESS - DO NOT USE


import microbit.GPIO as GPIO
import time

GPIO.setmode(GPIO.MICROBIT)

BUTTON = 0
LED = 1

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

try:
    while True:
        if GPIO.input(BUTTON) == False: # active low
            print("Button pressed")
            GPIO.output(LED, True)
            time.sleep(0.25)
            GPIO.output(LED, False)
            time.sleep(0.25)

finally:
    GPIO.cleanup()

# END