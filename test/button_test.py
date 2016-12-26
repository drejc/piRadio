# Simple script to test read button state (pressed / not pressed) for TFT buttons
# Buttons are located on pins 12, 16 and 18
# BCM (Broadcom SOC channel) numbers are 18, 23 and 24

import os
import sys

import RPi.GPIO as GPIO

# import needed modules
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from gpio.PushButtonTracker import PushButton

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# buttonUp = 18
# buttonMiddle = 23
# buttonDown = 24

#
# GPIO.setup(buttonUp, GPIO.IN, GPIO.PUD_UP)
# GPIO.setup(buttonMiddle, GPIO.IN, GPIO.PUD_UP)
# GPIO.setup(buttonDown, GPIO.IN, GPIO.PUD_UP)

upBtn = PushButton("Up", 18, GPIO.PUD_UP)
downBtn = PushButton("Down", 24, GPIO.PUD_UP)
middleBtn = PushButton("Middle", 23, GPIO.PUD_UP)

buttons = [upBtn, middleBtn, downBtn]

try:
	while True:

		for button in buttons:
			if button.clicked():
				print button.name

		#
		# if GPIO.input(buttonUp) == GPIO.LOW:
		# 	print ("Up")
		# elif GPIO.input(buttonMiddle) == GPIO.LOW:
		# 	print ("Middle")
		# elif GPIO.input(buttonDown) == GPIO.LOW:
		# 	print ("Down")
		# else:
		# 	print ("none")

		# time.sleep(0.5)

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
	GPIO.cleanup()                 # resets all GPIO ports used by this program