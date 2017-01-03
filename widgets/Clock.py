# displays time and day with date
import time
from datetime import datetime

from pygame.surface import Surface

from widgets import Style
from widgets.Label import Label


class Clock():
	def __init__(self, width, height):

		self.width = width
		self.height = height

		self.timeFormat = "%H:%M:%S"

		self.dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
		self.monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

		self.__oldTimeLabel = ""

	# vertical display
	def show(self, horizontal=False):

		if horizontal:
			self.time = Label(self.width , self.height * 0.70, Style.clock.color)
			self.date = Label(self.width, self.height * 0.30, Style.clock.color)

		else:
			self.time = Label(self.width, self.height * 0.70, Style.clock.color)
			self.date = Label(self.width, self.height * 0.30, Style.clock.color)

		timeLabel = self.getTimeCaption()

		if self.__oldTimeLabel == timeLabel: # dont refresh if not necessary
			pass

		dateLabel = self.getDateCaption()

		timeSurface = self.time.caption(timeLabel, Style.clock.label)
		dateSurface = self.date.caption(dateLabel, Style.clock_date)

		surface = Surface((self.width, self.height))
		surface.fill(Style.clock.color)

		if horizontal:

			offsetX = (self.width - self.time.width() - self.date.width()) / 2
			surface.blit(timeSurface, (offsetX, 0))

			offsetX = offsetX + self.date.width()
			surface.blit(dateSurface, (offsetX, 0))

		else:
			surface.blit(timeSurface, (0, 0))

			offsetY = self.height * 0.7
			surface.blit(dateSurface, (0, offsetY))

		self.__oldTimeLabel = timeLabel
		return surface

	def horizontal(self):
		return self.show(True)

	def getTimeCaption(self):
		return time.strftime(self.timeFormat)

	def getDateCaption(self):
		weekDay = self.dayNames[datetime.today().weekday()]
		return weekDay + " " + str(datetime.today().day) + " " + self.monthNames[datetime.today().month - 1]


