import RPi.GPIO as GPIO
import time

class PushButton():

	def __init__(self, name, gpioIn, gpioUpDown):

		self.name = name
		self.pin = gpioIn
		self.low = GPIO.PUD_UP == gpioUpDown

		GPIO.setup(gpioIn, GPIO.IN, gpioUpDown)

		self.pressed = False
		self.state = False

		self.clickTime = 0
		self.doubleClick = False
		pass

	# returns true while button is being pressed, or false when released
	def isPressed(self):

		if self.low:
			state = 1
		else:
			state = 0

		self.state = (GPIO.input(self.pin) == state) # button is being pushed down or not
		return self.state

	# returns true if button was pressed and released, otherwise false
	def clicked(self):

		if not self.pressed:
			self.pressed = self.isPressed() # detect press ... once detected

		if self.low:
			state = 0
		else:
			state = 1

		return (GPIO.input(self.pin) == state) and self.pressed # button was pushed but currently it is not

	# returns true if button was double clicked
	def doubleClicked(self):

		if (self.clicked()):

			# check if double click
			diff = time.time() - self.clickTime
			self.doubleClick = (diff * 1000) < 1000 # less than a second
			self.clickTime = time.time()

		double = self.doubleClick
		self.doubleClick = False
		return double