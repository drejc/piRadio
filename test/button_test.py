import sys, pygame
import RPi.GPIO as GPIO

from pygame.locals import *
import time
import subprocess
import os
import glob

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

pygame.init()

# prints out button info when pressed
def buttons_click():
