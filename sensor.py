import RPi.GPIO as GPIO
import time

vihrean_aika = 4 # length of green light
runtime=40  # code runtime
sensor_runtime=10  # wait time before forcing gars to red

#GPIO
PAINIKE=26
RED_AUTO=16
YEL_AUTO=20
GRE_AUTO=21
RED_HUMAN=5
GRE_HUMAN=4
MOTIONSENS=6

#GPIO setup
GPIO.setmode (GPIO.BCM)

GPIO.setup (GRE_AUTO, GPIO.OUT)
GPIO.setup (YEL_AUTO, GPIO.OUT)
GPIO.setup (RED_AUTO, GPIO.OUT)
GPIO.setup (RED_HUMAN, GPIO.OUT)
GPIO.setup (GRE_HUMAN, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.setup (MOTIONSENS, GPIO.IN)


#Normal condition (green for cars)
GPIO.output(GRE_AUTO, 1)
GPIO.output(YEL_AUTO, 0)
GPIO.output(RED_AUTO, 0)

GPIO.output(RED_HUMAN, 1)
GPIO.output(GRE_HUMAN, 0)


def check_sensor():
	print("checking sensor")
	stop = time.time() + sensor_runtime
	while time.time() < stop:
		sensor = GPIO.input(MOTIONSENS)

		if sensor == 0:
			print("no cars, changing to red")
			change_cars_red()
			return

	print("force changing cars to red")
	change_cars_red()


def change_cars_red():
	time.sleep(0.1)
	GPIO.output(GRE_AUTO, 0)
	GPIO.output(YEL_AUTO, 1)
	time.sleep(1)
	GPIO.output(YEL_AUTO, 0)
	GPIO.output(RED_AUTO, 1)
	GPIO.output(GRE_HUMAN, 1)
	GPIO.output(RED_HUMAN, 0)

def change_cars_green():
	GPIO.output(GRE_HUMAN, 0)
	GPIO.output(RED_HUMAN, 1)
	time.sleep(1)
	GPIO.output(YEL_AUTO, 1)
	time.sleep(1)
	GPIO.output(GRE_AUTO, 1)
	GPIO.output(YEL_AUTO, 0)
	GPIO.output(RED_AUTO, 0)

end = time.time() + runtime
while time.time() < end:

	button = GPIO.input (PAINIKE)

	if button == 1:
		print("button pushed")
		check_sensor()
		time.sleep(vihrean_aika)
		change_cars_green()

	time.sleep (0.1) # ilman tata prossukaytto 100%

print("koodi ohi")
GPIO.cleanup ()




