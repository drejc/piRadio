import RPi.GPIO as GPIO

class PushButton():

	def __init__(self, name, gpioIn, gpioUpDown):

		self.name = name
		self.pin = gpioIn
		self.low = GPIO.PUD_UP == gpioUpDown

		GPIO.setup(gpioIn, GPIO.IN, gpioUpDown)

		self.oldState = False
		self.state = False
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

		clicked = (GPIO.input(self.pin) == state) and self.pressed # button was pushed but currently it is not

		if clicked:
			self.pressed = False

		return clicked

