from pygame import font

from pygame.surface import Surface

class Label():
	def __init__(self, width, height, color):
		self.surface = Surface((width, height))
		self.color = color
		self.surface.fill(color)

	def caption(self, text, fontStyle):

		myfont = font.SysFont(fontStyle.font, fontStyle.size)
		self.size = myfont.size(text)

		offsetX = (self.surface.get_width() - self.size[0]) / 2
		offsetY = (self.surface.get_height() - self.size[1]) / 2

		self.surface.fill(self.color)
		label = myfont.render(text, True, fontStyle.color)

		self.surface.blit(label, (offsetX, offsetY))
		return self.surface

	def width(self):
		return self.size[0]

	def height(self):
		return self.size[1]