# tracks mouse movements and executes action bound to touch action
import pygame


class TouchTracker():

	def __init__(self):
		self.clear()
		pass

	# to be called when mouse button is pressed
	def mouseDown(self, x, y):
		self.storePosition(x, y)
		self.buttonPressed = True

	# to be called when mouse is moved
	def mouseMove(self, x, y):
		if self.buttonPressed:
			self.storePosition(x, y)

			if self.executeAction():
				self.clearPositions()

	# to be called when mouse button is released
	def mouseUp(self, x, y):
		self.executeAction()
		self.clear()

	# executes action upon state (button and movement)
	# returns True if action was triggered and False if not
	def executeAction(self):

		dX = self.data[0] - self.oldData[0]
		dY = self.data[1] - self.oldData[1]

		self.deltaX = self.deltaX + dX
		self.deltaY = self.deltaY + dY

		return False

	# stores mouse movement position
	def storePosition(self, x, y):
		if self.oldData[0] == -1:
			self.oldData = (x, y)
		else:
			self.oldData = self.data

		self.data = (x, y)
		pass

	# clears stored positions and set button as not pushed
	def clear(self):
		self.clearPositions()
		self.buttonPressed = False

	# clears stored positions
	def clearPositions(self):
		self.data = (-1, -1)
		self.oldData = self.data

		self.deltaX = 0
		self.deltaY = 0

	# reacts to pygame event
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
