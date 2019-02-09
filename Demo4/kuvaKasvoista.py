from picamera import PiCamera
import shutil
import cv2
import matplotlib
matplotlib.use('Agg') #jotta ei kayta nayttoa kuvan nayttamisessa
import matplotlib.pyplot as plt
import numpy as np

# Otetaan kuva

camera = PiCamera()
snap = "/home/pi/Desktop/openCVkokeilu/piKasvot/image.png"
camera.capture(snap)

# Katsotaan onko kuvassa kasvoja


#Muodostetaan kasvojen ja silmien ymparille laatikot
def markFaces(kasvot, kuva):
    print("Theres a face in your picture!")
    for (x, y, w, h) in kasvot:
        return cv2.rectangle(kuva, (x, y), (x + w, y + h), (255, 0, 0), 2)

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread(snap)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #kuva harmaaks
faces = face_cascade.detectMultiScale(gray, 1.3, 5) # karvojen sijainti (x,y,width, heigth)





# Jos on kasvot, faces on tyyppia np.array muuten tyypia tuple

if isinstance(faces, np.ndarray):
    img = markFaces(faces, img)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.savefig(snap)
else: print("There is no face in this!")



# movelatest image to the Website
shutil.copyfile(snap, '/home/pi/Pictures/image.jpg')
