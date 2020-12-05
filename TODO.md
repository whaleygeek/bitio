# New Architecture - requirements

This is a sketch of the new requirements, for an updated bitio package.

## 1. Roll a new .hex file

The embedded .hex file needs updating, to support the device with the
combined movement sensor and compass, and also now the V2 device.

## 2. Sensing and control features

The following features are proposed, but please see the section on
_accelerators_ below, as we suspect they may make it easier to implement
things like NeoPixels and enhanced radio support.

* GPIO
* NeoPixels
* Further radio support
* more gestures
* sound
* microphone on V2
* captouch on V2
 
## 3. Accelerators

An accelerator is a function that is downloaded to the target via the
raw REPL (essentially by typing in the definition via the REPL).

This accelerator function is then callable remotely by invoking it
via the raw REPL, with or without parameters as appropriate. 
The accelerator function performs some local operation, and might
output some data to be consumed by the host.

A typical use of an accelerator function would be to perform some
local sensing and computation, such as looking at the gesture sensing
results and making an informed decision as to whether a specific combined
gesture has been detected, and communicating this back to the host. 
The accelerator essentially removes the need for very fast polling, and if
the accelerator is written with a relatively fast run-to-completion time,
it itself may be polled at a slower rate, as long as the rate is fast enough
to give necessary computation time to the accelerator. There is a preference
on using delta timestamps in the accelerator for timing analysis.

Another use of an accelerator could be to communicate with a complex
device over SPI, handle all the command protocol and data exchange locally,
and send back simple status or data values to the host; thus reducing the
amount of control data that would have to flow regularly across the host/bit
interface.

Accelerators could be built into the flashed bitio.hex image, or they could
be downloaded to the device on demand. The latter is better, because it means
that the sensing and control facilities may be updated without having to
re-spin the bitio.hex file, and all managed at the host end. There might be
opportunities for user written accelerators that are app specific.

We expect the accelerators to be lazily-loaded, such that the first time they
are needed to be there by the host, the bitio host side library transfers them
to the device and remembers at the host end, that they have been loaded.

## 4. Reset detection and recovery

If the reset button is pressed or the device suffers any form of surprise
USB removal, the pyserial port on the host closes and connection is lost.
This usually causes an exception dump in Pyserial, and forces the user to
restart their program.

With the introduction of accelerator functions, this becomes more important,
as any wanted accelerators will need to be reloaded before they can be assumed
to be present.

## 5. Choice between auto-connect or programmed-connect.

One of the existing features of bitio that had equal praise and criticism
from a range of users, is the auto connect feature; just doing `import microbit`
will connect to the device and make all facilities available. It was designed
this way, so that code that was originally written on the micro:bit could
easily be transferred as-is to the host side, and had an identical API
and experience.

The criticism was that making something happen on import can have other
unintended concequences for packages. Also, it is impossible to connect to
more than one micro:bit simultaneously this way, as it is a singleton without
any form of handle.

The praise was that it worked simply and if all you wanted to do was display
an image, you needed 2 lines of code, and generally bitio programs started
off very simple without any setup. Also the auto-detect facility happens
lazily on first use, and users liked the fact that they didn't have to
go hunting for the device connection details, it all happened automatically.

A proposal for change, is to support both methods.

Thus, if you `import microbit` you will get the auto connect singleton. If
you use something like `from microbit import device` then use
`mb1 = device.connect(<optional identity info>)` you get a unique connection
to that device; thus, allowing multiple device support, and a more controlled
method of connection (such as when you press a TKInter button, for example).

We might also offer `device.find()` to do a search for microbits where
multiple are present, using the USB VID/PID to identify a UART device that
is indeed a micro:bit, to prevent other serial devices being mis-detected.

# 6. Mop up other projects

Other projects that may be completely replaceable with a new version of bitio
include:

* mb_gateway
* wireless robot controller

We will probably deprecate those projects, and put signposts to a new
bitio in place.

# 7. Proper PiPy support

Setup information was contributed by one of our users; it would be useful
if those who prefer to install with `pip` can do so.
