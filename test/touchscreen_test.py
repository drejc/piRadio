import sys, pygame
from pygame.locals import *
import time
import os

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()

def main():
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                print("screen pressed") #for debugging purposes
                                pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])

                                # write position directly on screen
                                # render text
                                label = myfont.render("Click " + str(pos[0]) + ", " + str(pos[1]), 1, (255, 255, 255))
                                screen.blit(label, (100, 100))

                                print(pos) #for checking

                        #ensure there is always a safe way to end the program if the touch screen fails
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        sys.exit()
        time.sleep(0.2)
        pygame.display.update()


size = width, height = 320, 240
screen = pygame.display.set_mode(size)

myfont = pygame.font.SysFont("monospace", 15)

main()
