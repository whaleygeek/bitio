# touched.py - demonstrates using pin touch

import microbit
import time

while True:
    time.sleep(0.1)
    if microbit.pin0.is_touched():
        print("Pin 0 touched")
