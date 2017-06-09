# counter.py - Demonstrate counting 00 to 99 using the WhaleySans font

import microbit
import time

for i in range(100):
    microbit.display.show(i)
    time.sleep(0.1)

time.sleep(4) # note, display auto clears on exit

# END
