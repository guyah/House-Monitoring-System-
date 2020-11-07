# Add here the modules you want to enable here
import time
import threading
from app.mac import mac, signals
 
@signals.initialized.connect

def send_message(message):
    #mac.send_message_to("hellops","96176313062@s.whatsapp.net")
    t = threading.Thread(target=checkReg)
    t.start() 
    #print("feteet")        
           
        #mac.send_message_to("hello guy","96176313062@s.whatsapp.net")
    #mac.send_message_to("hi elias","96176313062@s.whatsapp.net")
    #mac.send_message_to("Ok lol ana guy khalse w ta3e :p bfasserlik wa2ta teje ","96170540259@s.whatsapp.net")

def send_image(image):
    mac.send_image("current.jpg", "96176313062@s.whatsapp.net")
    #print("hiiii")
    #mac.send_image("current.jpg", "96176313062@s.whatsapp.net")
    
    
    
def checkReg():
    count = 0
    countOwner = 0
    #print("fetet check") 
    while True:
        file = open("testfile.txt","r")
       # print(file.read())
        #time.sleep(0.5);
        
        if(file.read() == "unknown person"):
            count += 1
            if(count > 50):
                time.sleep(5)
                print("okito")
                send_image("current.jpg")
                mac.send_message_to("Stranger Danger!","96176313062@s.whatsapp.net")
                #send_image("ok")
                count = 0
        else:
            count = 0;
        if(file.read() == "owner"):
        #countOwner = 1
         #   if(countOwner > 2):
            #time.sleep(2)
            print("Owner is home")
            mac.send_message_to("Welcome home guy","96176313062@s.whatsapp.net")
            #countOwner = 0
