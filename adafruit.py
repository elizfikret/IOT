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
AIO_KEY = "aio_NkBh29LVMK3WYWsTPX5monuSdySy"
AIO_CLIENT_ID = bytes('client_'+'12321','utf-8') #random


TEMP_FEED_ID = 'temp_feed'
PHOTO_FEED_ID = 'photos'
#AIO_CONTROL_FEED = "elifik/feeds/temp-feed"

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
    
temp_feed = bytes('{:s}/feeds/{:s}'.format(AIO_USER,TEMP_FEED_ID), 'utf-8')
photo_feed = bytes('{:s}/feeds/{:s}'.format(AIO_USER,PHOTO_FEED_ID), 'utf-8')





    
    
    
def send_data(data):
#    camera.init(0, format=camera.JPEG)
#    camera.flip(1)
    # left / right
#    camera.mirror(1)
    # framesize
#    camera.brightness(-1)
#   camera.quality(6)
    
    
    temp = esp32.raw_temperature() # read the internal temperature of the MCU, in Fahrenheit
    esp32.ULP()
    print(temp)
#    photo = take_photo()
    client.publish(temp_feed, bytes(str(temp), 'utf-8'),
                   qos=0)
#    client.publish(photo_feed, bytes(str(photo), 'utf-8'),
#                  qos=0)
    print("temp",str(temp))
    print("msg sent")
    
    
#def take_photo():
#    print("taking picture")
#    camera.framesize(camera.FRAME_240X240)
#   buf = camera.capture()
    
#    f = open('image.jpg','w')
#    f.write(buf)
#    f.close()   
    
   # print("image_read",image_read.encode("utf-8"))
#    converted_string = ubinascii.a2b_base64(f)
   # print(converted_string)
#    return converted_string
        
    

    
    