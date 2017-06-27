# std_image.py - Demonstrate the use of standard MicroPython images

import microbit
import time


for image in microbit.Image.STD_IMAGES:
    microbit.display.show(image)
    time.sleep(0.5)


