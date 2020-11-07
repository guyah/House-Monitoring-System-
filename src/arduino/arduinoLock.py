import serial
import time
#ma32oul tkoun l port 1410 --> eza 3al yamin 1420 eza 3al chmel 1410
ser = serial.Serial('/dev/cu.wchusbserial1420', 9600)
time.sleep(2)
#while True:
#time.sleep(0.2)
#2 ya3ne bi dawwe marten bi bote2
#3 ya3ne bi dawwe 5 marrat bser3a
ser.write(b'3')
print(ser.readline().decode())
    