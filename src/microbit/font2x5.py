# font2x5.py  07/06/2017  D.J.Whale
#
# This font allows two digits to be squashed side by side on a micro:bit 5x5 display.
#
# The font was christened as "WhaleySans" by PragmaticPhil on 07/06/2017

font_data = (
    # 0
    (
    "99",
    "99",
    "99",
    "99",
    "99"
    ),

    # 1
    (
    "09",
    "09",
    "09",
    "09",
    "09"
    ),

    # 2
    (
    "99",
    "09",
    "99",
    "90",
    "99"
    ),

    # 3
    (
    "99",
    "09",
    "99",
    "09",
    "99"
    ),

    # 4
    (
    "90",
    "90",
    "99",
    "09",
    "09"
    ),

    # 5
    (
    "99",
    "90",
    "99",
    "09",
    "99"
    ),

    # 6
    (
    "99",
    "90",
    "99",
    "99",
    "99"
    ),

    # 7
    (
    "99",
    "09",
    "09",
    "09",
    "09"
    ),

    # 8
    (
    "99",
    "99",
    "00",
    "99",
    "99"
    ),

    # 9
    (
    "99",
    "99",
    "99",
    "09",
    "99"
    )
)

def build_image_string(number):
    """Build a custom image string for MicroPython use"""
    #image = Image("90009:"
    #          "09090:"
    #          "00900:"
    #          "09090:"
    #          "90009")
    if type(number) != int:
        raise RuntimeError("Must provide an integer, got:%s" % str(type(number)))

    if number < 0 or number > 99:
        raise RuntimeError("Out of range number, must be 00..99, got:%d" % number)

    lg = font_data[int(number / 10)]
    rg = font_data[int(number % 10)]

    canvas = ""
    for r in range(5):
        canvas += lg[r] + "0" + rg[r]
        if r != 4:
            canvas += ':'

    return canvas



#----- TEST HARNESS -----------------------------------------------------------

if __name__ == "__main__":
    for i in range(100):
        s = build_image_string(i)
        print(i)
        print(s)
        print("")
# END



