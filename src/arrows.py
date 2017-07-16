import microbit

while True:
    for i in range(len(microbit.Image.ALL_ARROWS)):
        microbit.display.show(microbit.Image.ALL_ARROWS[i])
        microbit.sleep(100)