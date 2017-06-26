# api.py  01.06.2017  D.J.Whale
#
# an API to a remote micro:bit
#
# TODO: named Images
# TODO: user images
# TODO: for all pins: digital_write, digital_read
# TODO: for analog pins: analog_write, analog_read
# TODO: lots of other API methods that need implementing.

#Will have to resolve in display.show as:
#  display.show(Image.HEART)    <- no quotes
#  display.show(list of images) will have to resolve to:
#    display.show([Image.HEART, Image.HAPPY])    <- no quotes

# Want HEART to be an instance of something we can recognise
# as a StandardImage

class StandardImage():
    def __init__(self, name):
        self.name = name

class StandardImages():
    HEART       = StandardImage("HEART")
    HEART_SMALL = StandardImage("HEART_SMALL")
    HAPPY       = StandardImage("HAPPY")
    SMILE       = StandardImage("SMILE")
    SAD         = StandardImage("SAD")
    CONFUSED    = StandardImage("CONFUSED")
    ANGRY       = StandardImage("ANGRY")
    ASLEEP      = StandardImage("ASLEEP")
    SURPRISED   = StandardImage("SURPRISED")
    SILLY       = StandardImage("SILLY")
    FABULOUS    = StandardImage("FABULOUS")
    #MEH
    #YES
    #NO
    #TRIANGLE
    #TRIANGLE_LEFT
    #CHESSBOARD
    #DIAMOND
    #DIAMOND_SMALL
    #SQUARE
    #SQUARE_SMALL
    #RABBIT
    #COW
    #MUSIC_CROTCHET
    #MUSIC_QUAVER
    #MUSIC_QUAVERS
    #PITCHFORK
    #XMAS
    #PACMAN
    #TARGET
    #TSHIRT
    #ROLLERSKATE
    #DUCK
    #HOUSE
    #TORTOISE
    #BUTTERFLY
    #STICKFIGURE
    #GHOST
    #SWORD
    #GIRAFFE
    #SKULL
    #UMBRELLA
    #SNAKE
    #CLOCK12
    #CLOCK11
    #CLOCK10
    #CLOCK9
    #CLOCK8
    #CLOCK7
    #CLOCK6
    #CLOCK5
    #CLOCK4
    #CLOCK3
    #CLOCK2
    #CLOCK1
    #ARROW_N
    #ARROW_NE
    #ARROW_E
    #ARROW_SE
    #ARROW_S
    #ARROW_SW
    #ARROW_W
    #ARROW_NW

class MicroBit():
    def __init__(self, repl):
        self.repl                 = repl
        self.button_a.parent      = self
        self.button_b.parent      = self
        self.accelerometer.parent = self
        self.display.parent       = self
        self.pin0.parent          = self
        self.pin1.parent          = self
        self.pin2.parent          = self

    def cmd(self, command):
        ##print("send:%s" % command)
        self.repl.send_command(command)
        r = self.repl.wait_response()
        r = r.strip() # strip last NL from any print statement
        return r

    class TouchPin():
        def __init__(self, name):
            self.name = name

        def is_touched(self):
            r = self.parent.cmd("print(%s.is_touched())" % self.name)
            r = eval(r)
            return r

    class Button():
        def __init__(self, name):
            self.name = name

        def was_pressed(self):
            r = self.parent.cmd("print(%s.was_pressed())" % self.name)
            r = eval(r)
            return r

        def is_pressed(self):
            r = self.parent.cmd("print(%s.is_pressed())" % self.name)
            r = eval(r)
            return r

    class Accelerometer():
        def __init__(self, name):
            self.name = name

        def get_x(self):
            r = self.parent.cmd("print(%s.get_x())" % self.name)
            r = int(r)
            return r

        def get_y(self):
            r = self.parent.cmd("print(%s.get_y())" % self.name)
            r = int(r)
            return r

        def get_z(self):
            r = self.parent.cmd("print(%s.get_z())" % self.name)
            r = int(r)
            return r

        def get_values(self):
            r = self.parent.cmd("print(%s.get_values())" % self.name)
            r = r[1:-1] # remove brackets
            r = r.split(",")
            r = (int(r[0]), int(r[1]), int(r[2]))
            return r

    class Image():
        def __init__(self, bitmap_str):
            self.bitmap_str = bitmap_str

        def __str__(self):
            return self.bitmap_str

    class Display():
        def __init__(self, name):
            self.name = name

        def show(self, v):
            if isinstance(v, StandardImage):
                self.parent.cmd("%s.show(Image.%s)" % (self.name, v.name))
            elif isinstance(v, MicroBit.Image):
                s = v.__str__() # get bitmap
                self.parent.cmd("%s.show(Image(\"%s\"))" % (self.name, s))
            elif isinstance(v, str):
                self.parent.cmd("%s.show(\"%s\")" % (self.name, v))
            elif isinstance(v, int):
                if v >= 0 and v <= 99:
                    import font2x5
                    istr = font2x5.build_image_string(v)
                    self.parent.cmd("%s.show(Image(\"%s\"))" % (self.name, istr))
                else:
                    v = str(v)
                    self.parent.cmd("%s.show(\"%s\")" % (self.name, v))

        def clear(self):
            self.parent.cmd("%s.clear()" % self.name)



    button_a      = Button('button_a')
    button_b      = Button('button_b')
    accelerometer = Accelerometer("accelerometer")
    display       = Display("display")
    pin0          = TouchPin("pin0")
    pin1          = TouchPin("pin1")
    pin2          = TouchPin("pin2")
    Image         = StandardImages()

# END
