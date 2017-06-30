# repl/repl.py
#
# A REPL interface to a micro:bit or similar device running MicroPython
# This is written on top of pyserial, however the dependency on pyserial
# is soft (as the serial instance is passed in as a constructor parameter
# and the detection of the need to bytes-encode strings is dynamic).
# Thus you can pass in any object that implements the following interface:
#   write(str)
#   read()-> str
# and/or this interface:
#   write(bytes)
#   read()->bytes

import time
import re

class REPLException(Exception):
    def __init__(self, msg=None):
        Exception.__init__(self, msg)

class REPL():
    def __init__(self, ser):
        self.ser = ser
        def rx(): # always return a str(1) regardless of python version
            data = ser.read(1)
            if len(data) == 0:
                return None

            if type(data) == str: # pyserial2
                d = data[0]

            elif type(data) == bytes: # pyserial3
                d = data[0] # this will be a bytes() of len 1
                d = chr(d)

            else: # no idea!
                raise REPLException("Unknown return type from ser.read:%s" % str(type(data)))

            return d

        self.readch = rx

    def receive(self, wanted=None, min_length=None, max_length=None, timeout=None, idle_timeout=None):
        ##print("trying to receive:%s" % str(wanted))
        if wanted is not None:
            matcher = re.compile(wanted, re.DOTALL)
        else:
            matcher = None

        now = time.time()
        if timeout is not None:
            timeout_at = now + timeout
        else:
            timeout_at = None

        if idle_timeout is not None:
            idle_timeout_at = now + idle_timeout
        else:
            idle_timeout_at = None

        buffer = ""
        while True:
            now = time.time()
            ch = self.readch()
            if ch is not None:
                buffer += ch
                if idle_timeout is not None:
                    idle_timeout_at = now + idle_timeout

                if matcher is not None and idle_timeout is None and matcher.match(buffer):
                    if min_length is None:
                        ##print("got:%s" % buffer)
                        return buffer #TODO get captures
                    elif len(buffer) >= min_length:
                        ##print("got:%s" % buffer)
                        return buffer

                if max_length is not None and len(buffer) >= max_length:
                    raise REPLException("buffer overflow? [%s]" % buffer)

            if timeout_at is not None and now >= timeout_at:
                raise REPLException("Timeout trying to receive [%s]" % buffer)

            if idle_timeout_at is not None and now >= idle_timeout_at:
                if matcher is not None and matcher.match(buffer):
                    if min_length is None:
                        ##print("got:%s" % buffer)
                        return buffer
                    elif len(buffer) >= min_length:
                        return buffer
                        ##print("got:%s" % buffer)
                    else:
                        raise REPLException("Did not match at end of idle timeout, too short [%s]" % buffer)
                else:
                    raise REPLException("Did not match at end of idle timeout [%s]" % buffer)

    def to_raw(self):
        ##print("**** WAITING FOR PROMPT")
        if not self.wait_prompt():
            ##print("**** SENDING CTRL-C to force a prompt")
            self.ctrl_c() # try to stop running user program
            self.ctrl_b() # also if already at raw REPL, trigger exit from it
            ##print("**** waiting for prompt response")
            if not self.wait_prompt():
                raise REPLException("could not get a prompt")

        ##print("**** SENDING CTRL-A to get raw repl")
        self.ctrl_a() # enter raw REPL mode
        self.wait_repl_response()
        ##print("**** GOT RAW REPL")

    def wait_prompt(self):
        try:
            ##print("*** waiting for prompt")
            self.receive(".*>>> ", timeout=2, idle_timeout=1)
        except REPLException as e:
            ##print("*** REPLEXCEPTION:%s" % str(e))
            return False
        return True

    ##TODO: This does not work at all in Python 3, It seems to encode as b'\x00 \x00 \x00'
    #and as a result the REPL does not respond at all. But it works in Python 2 at the moment
    #still.
    # if we pass in chr(ord(code)-64) we get a 'can't handle unicode \x03' error in ser.write.
    # Note: Martin O'Hanlon said in BlueDot he wrote a to_bytes.
    # There is a to_bytes inside PySerial, but for some reason the REPL prompt is not
    # detected - perhaps that is less to do with byte encoding, and more to do with
    # string comparisons failing? Put some debug on this and see what actually is sent and returned.

    def ctrl_c(self):
        self.ser.write(b'\x03')

    def ctrl_a(self):
        self.ser.write(b'\x01')

    def ctrl_b(self):
        self.ser.write(b'\x02')

    def ctrl_d(self):
        self.ser.write(b'\x04')

    def wait_repl_response(self):
        self.receive("\r\nraw REPL; CTRL-B to exit\r\n>", timeout=2)

    def _send_command(self, cmd):
        self.ser.write(cmd)

    def send_command(self, cmd):
        #pyserial 3 or greater will not cope with strings, must be bytes
        #but we don't want a hard dependency to 'serial' module, and this is
        #not really a python3 thing, it's a pyserial thing.
        #We resolve this by catching the first TypeError and rewriting the wrapper
        #function for future calls.

        try:
            self._send_command(cmd)

        except TypeError:
            def _new_send_command(cmd):
                cmd = bytes(cmd, 'UTF-8')
                self.ser.write(cmd)
            self._send_command = _new_send_command
            self._send_command(cmd)

        self.ctrl_d()

    def wait_response(self):
        self.receive("OK", timeout=1, min_length=2)

        output_text = self.receive(".*\x04")
        exception_text = self.receive(".*\x04", timeout=1)
        output_text = output_text[:-1] # strip CTRL-D
        exception_text = exception_text[:-1] # strip CTRL-D

        self.receive(">", timeout=1)

        if exception_text != "":
            raise REPLException("REPL exception:%s" % exception_text)

        return output_text

# END
