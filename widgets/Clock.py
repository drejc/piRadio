# displays time and day with date
import calendar
import time

from pygame.surface import Surface

from widgets import Style
from widgets.Label import Label


class Clock():
	def __init__(self, width, height):
		self.time = Label(width, height * 0.66, Style.clock.color)
		self.date = Label(width, height * 0.34, Style.clock.color)

		self.width = width
		self.height = height

		self.timeFormat = "%H:%M:%S"
		self.dateFormat = "%d.%m.%Y"

	def show(self):
		timeLabel = time.strftime(self.timeFormat)
		dateLabel = time.strftime(self.dateFormat)

#		weekDay = calendar.day_name[time.time().weekday()]

		timeSurface = self.time.caption(timeLabel, Style.clock.label)
		dateSurface = self.date.caption(dateLabel, Style.clock_date)

		surface = Surface((self.width, self.height))
		surface.fill(Style.clock.color)

		offsetX = (self.width - self.time.widht()) / 2
		surface.blit(timeSurface, (offsetX, 0))

		offsetX = (self.width - self.date.widht()) / 2
		offsetY = self.height * 0.66
		surface.blit(dateSurface, (offsetX, offsetY))

		return surface



