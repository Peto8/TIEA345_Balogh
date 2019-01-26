import time
from picamera import PiCamera
import shutil

# take a basic picture
camera = PiCamera()

image = "/home/pi/Desktop/camdemo/image%s.jpg" % time.strftime("%H:%M:%S")

camera.capture(image)


# this being the latest picture, move to the Website
shutil.copyfile(image, '/home/pi/Pictures/image.jpg')
