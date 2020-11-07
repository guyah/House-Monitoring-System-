####################################################
# Modified by Nazmi Asri                           #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Import OpenCV2 for image processing
import cv2
# Import numpy for matrices calculations
import numpy as np
from multiprocessing import Pool
import os 
import time
import threading
import importlib
import subprocess

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def run_wp():
    os.system("python3 run.py")


subprocess.Popen("python3 run.py", shell=True)

# The hi_module can be used in order to interact with server (send commands to server and server can parse text and send back data)

#subprocess.Popen("python3 modules/hi_module.py", shell=True)


#thread.start_new_thread(run_wp(),("Thread"))
    #exec(compile(f.read(), "python3 run.py", 'exec'))
   
# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("trainer/")

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

#Used to send the stranger picture at a normal rate
strangeCount = 0

t = time.time()

tVid = time.time()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('nowVid.mp4',fourcc, 10.0, (1280,720))
# Loop
while True:
    
    # Read the video frame
    ret, im =cam.read()
    
    if((time.time() - tVid) >= 10):
        print("Writing video")
        out.write(im)
        if((time.time() - tVid) >= 28):
            print("Done")
            out.release()
            tVid = time.time()
    
    if((time.time() - t) >= 5):
            print("Saved")
            cv2.imwrite("now.jpg",im)
            t = time.time()
    
    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    
    # For each face in faces
    for(x,y,w,h) in faces:
        
        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (230,0,0), 4)
        
        # Recognize the face belongs to which ID
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        print("Id: " + str(Id) + "   Confidence: " + str(confidence))
        
        # Check the ID if exist 
        #if(Id == 1):
        #    Id = "Nazmi {0:.2f}%".format(round(100 - confidence, 2))
       
        
        #if (Id != 0):
            #time.sleep(1)
         #   print("We have some recognized faces")
        
        if(confidence < 30):
            strangeCount = 0
            file = open("testfile.txt","w")
            file.truncate()
            file.write("known person")
            #subprocess.Popen("python3 sendHelloGuy.py", shell=True)
            print("We have some recognized faces")
            # Put text describe who is in the picture
            face_Id = str(Id)
            if(Id == 1):
                face_Id = "Guy"
                file = open("testfile.txt","w")
                file.truncate()
                file.write("owner")
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, face_Id, (x,y-40), font, 1, (255,255,255), 3)
        else:
            strangeCount += 1
            file = open("testfile.txt","w")
            if(strangeCount > 10):
                file.write("unknown person")
                file.truncate()
                cv2.imwrite("current.jpg",im)
                strangeCount = 0
            print("Some faces were not recognized")
        
    #if (len(faces) > 0):
        
    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()


