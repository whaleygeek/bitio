import microbit

while True:
    for i in range(len(microbit.Image.ALL_CLOCKS)):
        microbit.display.show(microbit.Image.ALL_CLOCKS[i])
        microbit.sleep(100)