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
    HEART          = StandardImage("HEART")
    HEART_SMALL    = StandardImage("HEART_SMALL")
    HAPPY          = StandardImage("HAPPY")
    SMILE          = StandardImage("SMILE")
    SAD            = StandardImage("SAD")
    CONFUSED       = StandardImage("CONFUSED")
    ANGRY          = StandardImage("ANGRY")
    ASLEEP         = StandardImage("ASLEEP")
    SURPRISED      = StandardImage("SURPRISED")
    SILLY          = StandardImage("SILLY")
    FABULOUS       = StandardImage("FABULOUS")
    #MEH           = StandardImage("")
    #YES           = StandardImage("")
    #NO            = StandardImage("")
    #TRIANGLE      = StandardImage("")
    #TRIANGLE_LEFT = StandardImage("")
    #CHESSBOARD    = StandardImage("")
    #DIAMOND       = StandardImage("")
    #DIAMOND_SMALL= StandardImage("")
    #SQUARE= StandardImage("")
    #SQUARE_SMALL= StandardImage("")
    #RABBIT= StandardImage("")
    #COW= StandardImage("")
    #MUSIC_CROTCHET= StandardImage("")
    #MUSIC_QUAVER= StandardImage("")
    #MUSIC_QUAVERS= StandardImage("")
    #PITCHFORK= StandardImage("")
    #XMAS= StandardImage("")
    #PACMAN= StandardImage("")
    #TARGET= StandardImage("")
    #TSHIRT= StandardImage("")
    #ROLLERSKATE= StandardImage("")
    #DUCK= StandardImage("")
    #HOUSE= StandardImage("")
    #TORTOISE= StandardImage("")
    #BUTTERFLY= StandardImage("")
    #STICKFIGURE= StandardImage("")
    #GHOST= StandardImage("")
    #SWORD= StandardImage("")
    #GIRAFFE= StandardImage("")
    #SKULL= StandardImage("")
    #UMBRELLA= StandardImage("")
    #SNAKE= StandardImage("")
    #CLOCK12= StandardImage("")
    #CLOCK11= StandardImage("")
    #CLOCK10= StandardImage("")
    #CLOCK9= StandardImage("")
    #CLOCK8= StandardImage("")
    #CLOCK7= StandardImage("")
    #CLOCK6= StandardImage("")
    #CLOCK5= StandardImage("")
    #CLOCK4= StandardImage("")
    #CLOCK3= StandardImage("")
    #CLOCK2= StandardImage("")
    #CLOCK1= StandardImage("")
    #ARROW_N= StandardImage("")
    #ARROW_NE= StandardImage("")
    #ARROW_E= StandardImage("")
    #ARROW_SE= StandardImage("")
    #ARROW_S= StandardImage("")
    #ARROW_SW= StandardImage("")
    #ARROW_W= StandardImage("")
    #ARROW_NW= StandardImage("")

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
    ##TODO: Image         = StandardImages()

# END
