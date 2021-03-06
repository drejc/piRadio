import pygame.locals
import sys
import os

# install widget module
import time

from widgets import Style
from widgets.Clock import Clock
from widgets.Label import Label

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)


from widgets import Button

# Initialize the drawing window.
pygame.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
silver = (200, 200, 200)

size = width, height = 320, 240
screen = pygame.display.set_mode(size, 0, 32)
screen.fill(white)

button = Button.button(200, 20, "test")
screen.blit(button, (10, 5))


label = Label(200, 20, Style.Colors.white)
label.caption("Some dummy text", Style.clock_date)


screen.blit(label.surface, (10, 35))

screenClock = pygame.time.Clock()

clock = Clock(310, 50)

# screen.fill ((250, 250, 250))
# pygame.display.set_caption ('Draw.draw_rect ()')
#
# # Draw rectangles with various colors.
# rect = Draw.draw_rect (55, 40, (255, 0, 0))
# screen.blit (rect, (5, 5))
#
# rect = Draw.draw_rect (55, 40, (0, 255, 0))
# screen.blit (rect, (65, 5))
#
# rect = Draw.draw_rect (55, 40, (0, 0, 255))less
# screen.blit (rect, (125, 5))

# Draw encapsulated rectangles.
# for i in range (30):
#     val = i + 3
#     rnd = (random.randint (0, 5), random.randint (0, 5), random.randint (0, 5))
#     color = (rnd[0] * i + 100,  rnd[1] * i + 100, rnd[2] * i + 100)
#     rect = Draw.draw_rect (100 - 2 * val, 100 - 2 * val, color)
#     screen.blit (rect, (5 + val, 50 + val))

# Show anything.
pygame.display.flip()

clock.timeFormat = "%H:%M"

def main():

	while True:
		#pygame.display.update()

		#label.caption(str(time.time()), Style.clock_date)
		#screen.blit(label.surface, (10, 35))

		screen.blit(clock.show(), (5, 70))
		screen.blit(clock.horizontal(), (5, 120))

		for event in pygame.event.get():

			# ensure there is always a safe way to end the program if the touch screen fails
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()

		pygame.display.flip()
		screenClock.tick(24)

main()