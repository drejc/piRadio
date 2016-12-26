# draws button on x, y coordinate with w - width / h - height and label
from pygame import font, draw, Surface

from widgets import Style


def button(width, height, caption):
	# line thickness
	thickness = Style.button.border.thickness

	# background
	surface = Surface((width, height))
	surface.fill(Style.button.color)

	# border
	if thickness > 0:
		draw.lines(surface, Style.button.border.color, True,
		           [(0, 0), (width - thickness, 0), (width - thickness, height - thickness), (0, height - thickness)],
		           thickness)

	# label
	myfont = font.SysFont(Style.button.label.font, Style.button.label.size)
	size = myfont.size(caption)

	# center text ...
	offsetX = (width - size[0]) / 2
	offsetY = (height - size[1]) / 2

	# draw text on surface
	label = myfont.render(caption, True, Style.button.label.color)
	surface.blit(label, (offsetX, offsetY))

	return surface
