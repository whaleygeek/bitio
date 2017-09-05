# sensing.py - demonstrates sensing buttons and tilt

import time
import microbit

print("micro:bit connected - press buttons A to test")

while True:
    time.sleep(0.25)
    if microbit.button_a.was_pressed():
        print("Button A pressed")
        microbit.display.show("A")
        time.sleep(0.5)
        microbit.display.clear()

    if microbit.button_b.was_pressed():
        print("Button B pressed")
        microbit.display.show("B")
        time.sleep(0.5)
        microbit.display.clear()

    print(microbit.accelerometer.get_values())


# END
