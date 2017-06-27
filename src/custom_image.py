# custom_image.py - show how to define and use a custom image

import microbit
import time

SQUARE = microbit.Image("99999:90009:90009:90009:99999")
microbit.display.show(SQUARE)
time.sleep(4)

# END

