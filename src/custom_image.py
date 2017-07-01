# custom_image.py - show how to define and use a custom image

import microbit
import time

BANANA = microbit.Image("00090:00090:00990:09900:99000")
microbit.display.show(BANANA)
time.sleep(4)

# END

