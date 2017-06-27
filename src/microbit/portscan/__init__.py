# portscan.py  22/04/2014  D.J.Whale
#
# Prompt user and find a newly inserted com port
# Appropriately configured this should work on mac and linux

import time

# CONFIGURATION ========================================================

# The file that will be created to cache the found port name
CACHE_NAME = "portscan.cache"

# The time, in seconds, to wait for any drivers to unload.
# When the user presses ENTER after the "remove device" message,
# it sometimes takes some computers a little bit of time to safely
# unload the driver. This prevents false readings.
DRIVER_UNLOAD_TIME = 2

# The time, in seconds, to wait for any drivers to load.
# When the user presses ENTER after the "insert device" message,
# it sometimes takes some computers a little bit of time to safely
# load the driver. This prevents false readings.

DRIVER_LOAD_TIME = 4

def message(msg):
  print(msg)
  
def nl():
  print("\n")


# SYSTEM AND VERSION VARIANCE ==========================================

import sys
import os

if sys.version_info.major >= 3:
  ask = input
else:
  ask = raw_input
    
if os.name == 'nt': #sys.platform == 'win32':
    try:
      import ports_win32 as ports
    except ImportError:
      from . import ports_win32 as ports
elif os.name == 'posix':
    try:
      import ports_unix as ports
    except ImportError:
      from . import ports_unix as ports
else:
    raise ImportError("No port lister available for:" + os.name)


# HELPERS ==============================================================

def getYesNo(msg):
  """ Ask user for yes/no and return a boolean """
  answer = ask(msg + " (Y/N)")
  answer = answer.upper()
  if answer in ['YES', 'Y']:
    return True
  return False
  
def getAdded(before, after):
  """ Find any items in 'after' that are not in 'before' """

  #message("before:" + str(before))
  #message("after:" + str(after))
  
  # Any items in 'before' are removed from 'after'
  # The remaining list is of the newly added items
  
  for b in before:
    try:
      i = after.index(b)
      after.remove(b)
    except ValueError:
      pass

  #message("new:" + str(after))
  return after  
  
  
# BODY =================================================================

def scan():
  """ scan devices repeatedly until new one found, or user gives in """
  message("Scanning for serial ports")
  while True:
    # prompt to remove device
    ask("remove device, then press ENTER")

    message("scanning...")
    time.sleep(DRIVER_UNLOAD_TIME) # to allow driver to unload
    before = ports.scan()
    beforec = len(before)
    message("found " + str(beforec) + " devices")

    # prompt to insert device
    ask("plug in device, then press ENTER")

    message("scanning...")
    time.sleep(DRIVER_LOAD_TIME) # to allow driver to load
    after = ports.scan()
    afterc = len(after)
    message("found " + str(afterc) + " devices")

    # diff the lists
    added = getAdded(before, after)
    
    if len(added) == 0:
      # No new ones, try again?
      message("no new devices detected")
      yes = getYesNo("Try again?")
      if yes:
        continue
      return None
    
    elif len(added) > 1:
      # Show a menu and get a choice
      while True:
        message("more than one new device found")
        for i in range(len(added)):
          message(str(i+1) + ":" + added[i])
        a = ask("which device do you want to try?")
        try:
          a = int(a)
          if a < 1 or a > len(added):
            message("out of range, try again")
            continue
          a -= 1
          return added[a]
        except:
          pass

    else: 
      # only 1 new, select it
      message("found 1 new device")
      dev = added[0]
      message("selected:" + dev)
      return dev
      
    
def remember(device):
  """ Remember this device for next time """
  # prompt if you want it remembered
  yes = getYesNo("Do you want this device to be remembered?")

  if yes:
    # Remember it
    f = open(CACHE_NAME, "w")
    f.write(device + "\n")
    f.close()

def find():
  """ Try to find a newly inserted device, by prompting user """
  dev = scan()
  if dev != None:
    remember(dev)
  return dev
  
def forget():
  """forget the remembered cached name if stored"""
  # Remove any existing cache file
  try:
    os.remove(CACHE_NAME)
  except:
    pass
  
def getName():
  """read the remembered cached named, None if none stored"""
  try:
    f = open(CACHE_NAME, "r")
    name = f.readline().strip()
    f.close()
    return name  
  except IOError:
    message("No device has previously been detected")
    return None

def main():
  message("*" * 79)
  message("SERIAL PORT SCANNER PROGRAM")
  message("*" * 79)
  
  n = getName()
  if n == None:
    message("No name remembered")
  else:
    message("Already remembered:" + n)
    message("forgetting...")
    forget()
    
  d = find()
  if d == None:
    message("nothing found")
  else:
    message("found device:" + d)

# TESTER  
if __name__ == "__main__":
  main()
  
# END
