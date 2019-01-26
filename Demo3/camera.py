from picamera import PiCamera
import RPi.GPIO as GPIO
import time

# The sensor is checked every second, if it sees movement it captures a single picture and sleeps for 3s.

MOTIONSENS = 6
sensor_runtime = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTIONSENS, GPIO.IN)

camera = PiCamera()

stop = time.time() + sensor_runtime
while time.time() < stop:
    sensor = GPIO.input(MOTIONSENS)

    if sensor == 0:
        print("no movement")

    else:
        print("movement")
        camera.capture("/home/pi/Desktop/camdemo/image%s.jpg" % time.strftime("%H:%M:%S"))
        time.sleep(3)

    time.sleep(1)
