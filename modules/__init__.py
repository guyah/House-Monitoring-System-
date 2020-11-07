# Add here the modules you want to enable here
import time
from app.mac import mac, signals
@signals.initialized.connect
def send_message(message):
    mac.send_message_to("Connected","96176313062@s.whatsapp.net")
    #while True:
     #   time.sleep(3);
      #  mac.send_message_to("hello guy","96176313062@s.whatsapp.net")
    #mac.send_message_to("hi elias","96176313062@s.whatsapp.net")
    #mac.send_message_to("Ok lol ana guy khalse w ta3e :p bfasserlik wa2ta teje ","96170540259@s.whatsapp.net")
def send_image(image):
    print("hi")
    #mac.send_image("/Users/guy/Desktop/testt.png", "96176313062@s.whatsapp.net")
    #mac.send_image("/Users/guy/Desktop/testt.png", "96176313062@s.whatsapp.net")
