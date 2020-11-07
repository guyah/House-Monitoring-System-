from app.mac import mac, signals

import time
@signals.message_received.connect
def handle(message):
    #message.log() to see message object properties
    print("m : " + message.message)
    if((str(message.message)) == "Vid Now"):
        print("Sending now vid")
        mac.send_message_to("Taking live video",message.conversation)
        mac.send_video("nowVid.mp4", message.conversation)
    