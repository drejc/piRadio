# tracks mouse movements and executes action bound to touch action
import pygame


class TouchTracker():
	buttonPressed = False
	data = (0, 0)


	# to be called when mouse button is pressed
	def mouseDown(self, x, y):
		self.buttonPressed = True

	# to be called when mouse is moved
	def mouseMove(self, x, y):
		if self.buttonPressed:
			self.storePosition(x, y)

			if (self.executeAction()):
				self.clearPositions()


	# to be called when mouse button is released
	def mouseUp(self, x, y):
		self.buttonPressed = False
		self.executeAction()


	# executes action upon state (button and movement)
	# returns True if action was triggered and False if not
	def executeAction(self):
		return False


	# stores mouse movement position
	def storePosition(self, x, y):
		self.data = (x, y)
		pass


	# clears stored positions and set button as not pushed
	def clear(self):
		self.data = []
		self.buttonPressed = False


	# clears stored positions
	def clearPositions(self):
		self.data = []


	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			self.mouseDown(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

		if event.type == pygame.MOUSEMOTION:
			self.mouseMove(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

		if event.type == pygame.MOUSEBUTTONUP:
			self.mouseUp(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

		pass

	def x(self):
		return self.data[0]

	def y(self):
		return self.data[1]
