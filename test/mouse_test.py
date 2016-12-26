import sys
import pygame
import os

# install events and widgets module
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from events.TouchTracker import TouchTracker
from widgets import Style

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()

def main():
	while True:
		for event in pygame.event.get():

			tracker.event(event)

			screen.fill(white)

			label = myfont.render("Click " + str(tracker.x()) + ", " + str(tracker.y()), 1, Style.Colors.red)
			label2 = myfont.render("Moved " + str(tracker.deltaX) + ", " + str(tracker.deltaY), 1, Style.Colors.red)

			screen.blit(label, (100, 100))
			screen.blit(label2, (100, 120))

			pygame.display.update()



			# ensure there is always a safe way to end the program if the touch screen fails
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()


white = (255, 255, 255)
black = (0, 0, 0)

size = width, height = 320, 240
screen = pygame.display.set_mode(size, 0, 32)
screen.fill(white)
pygame.display.update()


tracker = TouchTracker()



myfont = pygame.font.SysFont("Arial", 15)

main()
