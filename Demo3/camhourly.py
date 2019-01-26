import time
from picamera import PiCamera

camera = PiCamera()

camera.capture("/home/pi/Desktop/camdemo/image%s.jpg" % time.strftime("%H:%M:%S"))
