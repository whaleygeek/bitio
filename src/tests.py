import unittest
import sys
import time
import microbit

def extract_ut_args():
    """Extract unittest specific arguments from sys.argv"""
    # -h -v -q -f -c -b
    # --locals
    # anything not starting with a -

    newargs = []
    for i in range(1, len(sys.argv)): # must ignore progname in argv[0]
        arg = sys.argv[i]
        if arg in ["-h", "-v", "-q", "-f", "-c", "-b", "--locals"]:
            newargs.append(arg)
        elif arg[0] != "-":
            newargs.append(arg)

    for arg in newargs:
        if arg in sys.argv:
            i = sys.argv.index(arg)
            del sys.argv[i]

    newargs.insert(0, sys.argv[0])
    return newargs

class TestButtons(unittest.TestCase):
    def test_ButtonA(self):
        print("press button A...")
        while True:
            time.sleep(0.25)
            if microbit.button_a.was_pressed():
                print("Button A pressed")
                break

    def test_ButtonB(self):
        print("press button B...")
        while True:
            time.sleep(0.25)
            if microbit.button_b.was_pressed():
                print("Button B pressed")
                break



if __name__ == "__main__":
    unittest.main(argv=extract_ut_args())
