from app.mac import mac, signals

import time
import serial
import time
import subprocess

@signals.message_received.connect
def handle(message):
    #message.log() to see message object properties
    
    print("m : " + message.message)
    if((str(message.message)) == "now"):
        print("Sending now")
        mac.send_image("now.jpg", message.conversation)
    if((str(message.message)) == "Open Door"):
        print("Door opened")
        mac.send_message_to("Front door opened","96176313062@s.whatsapp.net")
        subprocess.Popen("python3 arduino.py", shell=True)
    if((str(message.message)) == "Lock Door"):
        print("Door locked")
        mac.send_message_to("Front door locked","96176313062@s.whatsapp.net")
        subprocess.Popen("python3 arduinoLock.py", shell=True)
        
    #mac.send_video("path/to/video.mp4", message.conversation)