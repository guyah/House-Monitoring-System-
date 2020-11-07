from app.mac import mac, signals
from VideoCapture import Device

import time
@signals.message_received.connect
def handle(message):
    #message.log() to see message object properties
    if(str(message.message) == "status"):
    #mac.send_message("Hello", message.conversation)
        print("Sending status")
        mac.send_image("/Users/guy/Desktop/testt.png", message.conversation)
   
    #mac.send_video("path/to/video.mp4", message.conversation)