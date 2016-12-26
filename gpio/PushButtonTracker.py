import RPi.GPIO as GPIO


def callback(self):
	self.pressed = True
	pass


class PushButton():

	def __init__(self, name, gpioIn, gpioUpDown):

		self.name = name
		self.pin = gpioIn
		self.low = GPIO.PUD_UP == gpioUpDown

		GPIO.setup(gpioIn, GPIO.IN, pull_up_down=gpioUpDown)
		pass


	def isPressed(self):

		if self.low:
			state = 0
		else:
			state = 1

		return GPIO.input(self.pin) == state