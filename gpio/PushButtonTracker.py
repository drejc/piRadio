import RPi.GPIO as GPIO

class PushButton():

	def __init__(self, name, gpioIn, gpioUpDown):

		self.name = name
		self.pin = gpioIn
		self.low = GPIO.PUD_UP == gpioUpDown

		GPIO.setup(gpioIn, GPIO.IN, gpioUpDown)
		pass


	def isPressed(self):

		if self.low:
			state = GPIO.LOW
		else:
			state = GPIO.HI

		return GPIO.input(self.pin) == state