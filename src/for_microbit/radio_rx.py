# load this on micro:bit to receive messages sent by bitio

from microbit import *
import radio

radio.on()
print("Radio ON")
display.show(Image.HEART)

while True:
    try:
        incoming = radio.receive()
        if incoming:
            print(incoming)
            display.show(Image.DIAMOND)
            sleep(500)
            display.show(".")

    except:
        print("resetting radio")
        display.show(Image.NO)
        radio.off()
        radio.on()
        display.show(Image.HEART)
