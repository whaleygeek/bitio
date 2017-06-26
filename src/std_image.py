# std_image.py - Demonstrate the use of standard MicroPython images

import microbit
import time

# list: Image.ALL_CLOCKS
# list: Image.ALL_ARROWS

IMAGES = [
    microbit.Image.HEART,
    microbit.Image.HEART_SMALL,
    microbit.Image.HAPPY,
    microbit.Image.SMILE,
    microbit.Image.SAD,
    microbit.Image.CONFUSED,
    microbit.Image.ANGRY,
    microbit.Image.ASLEEP,
    microbit.Image.SURPRISED,
    microbit.Image.SILLY,
    microbit.Image.FABULOUS,
    #Image.MEH,
    #Image.YES,
    #Image.NO,
    #Image.TRIANGLE,
    #Image.TRIANGLE_LEFT,
    #Image.CHESSBOARD,
    #Image.DIAMOND,
    #Image.DIAMOND_SMALL,
    #Image.SQUARE,
    #Image.SQUARE_SMALL,
    #Image.RABBIT,
    #Image.COW,
    #Image.MUSIC_CROTCHET,
    #Image.MUSIC_QUAVER,
    #Image.MUSIC_QUAVERS,
    #Image.PITCHFORK,
    #Image.XMAS,
    #Image.PACMAN,
    #Image.TARGET,
    #Image.TSHIRT,
    #Image.ROLLERSKATE,
    #Image.DUCK,
    #Image.HOUSE,
    #Image.TORTOISE,
    #Image.BUTTERFLY,
    #Image.STICKFIGURE,
    #Image.GHOST,
    #Image.SWORD,
    #Image.GIRAFFE,
    #Image.SKULL,
    #Image.UMBRELLA,
    #Image.SNAKE,
    #Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1,
    #Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW
]

for image in IMAGES:
    microbit.display.show(image)
    time.sleep(0.5)


