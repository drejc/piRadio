import tkinter as tk

import time
from datetime import datetime

class TopLine(tk.Frame):

	def __init__(self, master, width, height):

		tk.Frame.__init__(self, master)
		self.pack()

		self.width = width
		self.height = height

		self.frame = tk.Frame

		self.timeFormat = "%H:%M:%S"

		self.dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
		self.monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

		fontsize = 12
		textwidth = 9

# TODO fix display
		self.LocalDate = tk.StringVar()
		self.LocalDate.set('waiting...')
		tk.Label(self, font=('Helvetica', fontsize), bg='white', fg='black', width=textwidth,
		         textvariable=self.LocalDate).grid(row=0, column=0)

		self.LocalTime = tk.StringVar()
		self.LocalTime.set('waiting...')
		tk.Label(self, font=('Helvetica', fontsize), bg='white', fg='black', width=textwidth,
		         textvariable=self.LocalTime).grid(row=0, column=1)

		self.refresh()
	pass

	def setDate(self, dateLabel):
		self.LocalDate.set(dateLabel)
	pass

	def setTime(self, timeLabel):
		self.LocalTime.set(timeLabel)
	pass

	def refresh(self):

		weekDay = self.dayNames[datetime.today().weekday()]
		weekDay = weekDay + " " + str(datetime.today().day) + " " + self.monthNames[datetime.today().month - 1]

		self.setDate(weekDay)

		self.setTime(time.strftime(self.timeFormat))
		self.after(1000, self.refresh)
	pass
