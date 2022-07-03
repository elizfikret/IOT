import network
 
def connect():
  ssid = "VIVACOM_FiberNet_93D4"
  password =  "zaniK2KMcs"
 
  station = network.WLAN(network.STA_IF)
 
  if station.isconnected() == True:
      print("Already connected")
      print(station.ifconfig())
      return
 
  station.active(True)
  station.connect(ssid, password)
 
  while station.isconnected() == False:
      pass
 
  print("Connection successful")
  print(station.ifconfig())
