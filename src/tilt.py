import microbit
import time

while True:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()

    if x < -300:
        print("left")
    elif x > 300:
        print("right")

    if y < -300:
        print("forward")
    elif y > 300:
        print("backward")

    time.sleep(0.5)
