# api.py  01.06.2017  D.J.Whale
#
# an API to a remote micro:bit
#
# TODO: for all pins: digital_write, digital_read
# TODO: for analog pins: analog_write, analog_read
# TODO: named Images
# TODO: lots of other API methods that need implementing.

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
            if isinstance(v, MicroBit.Image):
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


# END
