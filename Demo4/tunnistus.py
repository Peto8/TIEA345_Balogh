import cv2
import matplotlib
matplotlib.use('Agg') #jotta ei kayta nayttoa
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')

img = cv2.imread('kasvot1.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #kuva harmaaks

faces = face_cascade.detectMultiScale(gray, 1.3, 5) # karvojen sijainti (x,y,width, heigth)

#Muodostetaan kasvojen ja silmien ymparille laatikot

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.savefig("kasvot2.png")
