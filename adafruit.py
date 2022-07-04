import network      # For operation of WiFi network
import esp32
import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient  # For use of MQTT protocol to talk to Adafruit IO
from wifiConnect import *
import ubinascii              # Needed to run any MicroPython code
import sys
from machine import Pin, Timer               # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import camera

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "elifik"
AIO_KEY = "aio_gULP94mmfedtcIParTmfUz5bhqGs"
AIO_CLIENT_ID = bytes('client_'+'12321','utf-8') #random
AIO_TEMP_FEED = "elifik/feeds/temp-feed"

esp32.hall_sensor()     # read the internal hall sensor

 
connect()
   
    
# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

# Subscribed messages will be delivered to this callback
try:
    client.connect()
    print(" MQTT Connected")

except Exception as e:
    print("count not connect to MQTT server{}{}".format(type(e)._name_,e))
    sys.exit()
    

def send_data(data):

    temp = esp32.raw_temperature() # read the internal temperature of the MCU, in Fahrenheit
    esp32.ULP()
    print(temp)

    client.publish(AIO_TEMP_FEED, bytes(str(temp), 'utf-8'),
                   qos=0)
    print("temp",str(temp))
    print("msg sent")
    
