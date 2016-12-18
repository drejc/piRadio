# Simple script to test read button state (pressed / not pressed) for TFT buttons
# Buttons are located on pins 12, 16 and 18
# BCM (Broadcom SOC channel) numbers are 18, 23 and 24

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buttonUp = 18
buttonMiddle = 23
buttonDown = 24

GPIO.setup(buttonUp, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(buttonMiddle, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(buttonDown, GPIO.IN, GPIO.PUD_UP)

while True:
	if GPIO.input(buttonUp) == GPIO.LOW:
		print ("Up")
	elif GPIO.input(buttonMiddle) == GPIO.LOW:
		print ("Middle")
	elif GPIO.input(buttonDown) == GPIO.LOW:
		print ("Down")
	else:
		print ("none")

	time.sleep(0.5)
