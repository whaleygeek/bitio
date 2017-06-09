A REPL wrapper to MicroPython running on the micro:bit

The serial package is not imported due to python 2/3 package import complexities that need solving.
However, a serial instance is passed at runtime to REPL, which is enough for it to work.

