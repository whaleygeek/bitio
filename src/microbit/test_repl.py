# test_repl.py

import serial
from repl import REPL
import repl
# This is only a test. The real device port will be acquired by other means,
# such as portscan

def test():
    PORT = '/dev/tty.usbmodem1412'
    BAUD = 115200

    def get_serial():
        s = serial.Serial(PORT)
        s.baudrate = BAUD
        s.parity   = serial.PARITY_NONE
        s.databits = serial.EIGHTBITS
        s.stopbits = serial.STOPBITS_ONE
        s.timeout = 0 # non blocking mode

        s.close()
        s.port = PORT
        s.open()
        return s

    s = get_serial()

    repl = REPL(s)
    repl.to_raw()

    repl.send_command("print('hello')")
    print(repl.wait_response())

    repl.send_command("a=1")
    repl.wait_response()

    repl.send_command("print(a)")
    print(repl.wait_response())

    # FINISHED

    s.close()

if __name__ == "__main__":
    test()