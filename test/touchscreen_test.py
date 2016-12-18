import os
import pygame
import sys
import time

from pygame.locals import *

from widgets import Style

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()


def main():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("screen pressed")  # for debugging purposes
				print(Style.Colors.white)

				pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

				# write position directly on screen
				# render text
				screen.fill(white)

				label = myfont.render("Click " + str(pos[0]) + ", " + str(pos[1]), 1, black)
				screen.blit(label, (100, 100))
				pygame.display.update()

				print(pos)  # for checking

			# ensure there is always a safe way to end the program if the touch screen fails
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()
	time.sleep(0.2)
	pygame.display.update()


white = (255, 255, 255)
black = (0, 0, 0)

size = width, height = 320, 240
screen = pygame.display.set_mode(size, 0, 32)
screen.fill(white)
pygame.display.update()

myfont = pygame.font.SysFont("Arial", 15)

main()
