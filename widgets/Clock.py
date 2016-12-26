# displays time and day with date
import time
from datetime import datetime

from pygame.surface import Surface

from widgets import Style
from widgets.Label import Label


class Clock():
	def __init__(self, width, height):


		self.time = Label(width, height * 0.70, Style.clock.color)
		self.date = Label(width, height * 0.30, Style.clock.color)

		self.width = width
		self.height = height

		self.timeFormat = "%H:%M:%S"

		self.dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
		self.monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

		self.__oldTimeLabel = ""

	def show(self):
		timeLabel = time.strftime(self.timeFormat)

		if self.__oldTimeLabel == timeLabel: # dont refresh if not necessary
			pass


		weekDay = self.dayNames[datetime.today().weekday()]
		dateLabel = weekDay + " " + str(datetime.today().day) + " " + self.monthNames[datetime.today().month - 1]

		timeSurface = self.time.caption(timeLabel, Style.clock.label)
		dateSurface = self.date.caption(dateLabel, Style.clock_date)

		surface = Surface((self.width, self.height))
		surface.fill(Style.clock.color)

		offsetX = (self.width - self.time.widht()) / 2
		surface.blit(timeSurface, (offsetX, 0))

		offsetX = (self.width - self.date.widht()) / 2
		offsetY = self.height * 0.7
		surface.blit(dateSurface, (offsetX, offsetY))

		self.__oldTimeLabel = timeLabel
		return surface



