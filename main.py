import network
import camera
import socket
from adafruit import *
import esp32
import time
from machine import Pin, Timer               # Interfaces with hardware components

# #setup the Wifi connection
connect()

#initialize camera

try:
    camera.init(0, format=camera.JPEG)
    
except Exception as e:
    camera.deinit()
    camera.init(0, format=camera.JPEG)
    # Image settings ----------------------------
    ## Other settings:
    # flip up side down
    camera.flip(1)
    # left / right
    camera.mirror(1)
    # framesize
    
    camera.brightness(-1)
    camera.quality(6)


def take_photo():
    print("taking picture")
    camera.framesize(camera.FRAME_240X240)
    buf = camera.capture()
    f = open('image.jpg','w')
    f.write(buf)
    f.close()
    
#Setup the Web Server
    #AF_INET - use Internet Protocol v4 addresses
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
    

while True:
   
    take_photo()
    
    s.listen(80) #listen to incoming requests on port 80
    conn, addr = s.accept()
    print('got connection from %s' % str(addr))

    
    #process the requested filename
    request = conn.recv(1024)
    request = str(request)
    string_list = request.split(' ')
    #used to be sring_list[0] I changed it
    method = string_list[0]
    requesting_file = string_list[1]
    
    
    myfile = requesting_file.split('?')[0]
    myfile=myfile.lstrip('/')
    
    timer = Timer(0)
    timer.init(period=5000, mode=Timer.PERIODIC, callback=send_data)
 
    if(myfile == ''):
        myfile = 'index.html'
        print("myfile",myfile)
    try:
        #Serve up the file
        file = open(myfile,'rb')
        print("file",file)
        response = file.read()
        file.close()
            
        # build a header response
        header = 'HTTP/1.1 200 OK\n'
        if(myfile.endswith(".jpg")):
            mimetype = 'image/jpg'
        elif(myfile.endswith(".css")):
            mimetype = 'text/css'
        else:
            mimetype = 'text/html'
        header += 'Content Type: ' + str(mimetype) + '\n\n'
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3></center></body></html>'

    final_response = header.encode('utf-8')
    final_response += response
    try:
        conn.send(final_response)
    except:
        print("there was an error, resetting")
    conn.close()
    
        


  
    
