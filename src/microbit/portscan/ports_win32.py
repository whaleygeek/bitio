# ports_win32.py  22/04/2014  D.J.Whale
#
# Scan the windows registry to find a list of COM ports

try:
  import _winreg as registry # python2
except ImportError:
  import winreg as registry # python3

KEY = r"HARDWARE\DEVICEMAP\SERIALCOMM"

def scan():
  ports = []

  reg = registry.ConnectRegistry(None, registry.HKEY_LOCAL_MACHINE)
  try:
    key = registry.OpenKey(reg, KEY)
  except:
    # If there is no SERIALCOMM registry entry
    # it means this computer has never seen a serial port.
    # Best action is to return an empty ports list. 
    # When the device is inserted, windows will create the entry for us.
    return ports

  i = 0
  while True:
    try:
      value = registry.EnumValue(key, i)   
      name, value, vtype = value
      print("port[" + str(i) + "]:" + str(value))
      ports.append(value)
      i += 1
    
    except EnvironmentError:
      break
    
  return ports


# TESTER

if __name__ == "__main__":
  d = scan()
  print(str(d))
  
# END
