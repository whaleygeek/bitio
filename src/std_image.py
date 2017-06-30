# std_image.py - Demonstrate the use of standard MicroPython images

import microbit
import time

# show all the images on the display, one by one

for image in microbit.Image.STD_IMAGES:
    microbit.display.show(image)
    time.sleep(0.5)

# show a printable list of all image names

print(microbit.Image.STD_IMAGE_NAMES)

