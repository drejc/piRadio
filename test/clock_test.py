import pygame.locals
import sys
import os
import RPi.GPIO as GPIO

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from widgets import Style
from widgets.Clock import Clock

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()

# Initialize the drawing window.
pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size, 0, 32)
screen.fill(Style.Colors.white)

clock = Clock(310, 50)

# Show anything.
pygame.display.flip()

from gpio.PushButtonTracker import PushButton

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
downBtn = PushButton("Down", 24, GPIO.PUD_UP)

def main():

	while True:
		pygame.display.update()
		screen.blit(clock.show(), (5, 70))

		if downBtn.doubleClicked():
			sys.exit()

main()

GPIO.cleanup()                 # resets all GPIO ports used by this program