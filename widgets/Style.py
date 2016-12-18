import collections

from pygame import Color

# List of basic colors
class Colors():

	white = Color(255, 255, 255)
	black = Color(0, 0, 0)
	silver = Color(192, 192, 192)

	def __setattr__(self, *_):
		pass

Colors = Colors()

# basic styling ...

# Button
Button_Border = collections.namedtuple('Button_Border', 'color thickness')
Button_Label = collections.namedtuple('Button_Label', 'color font size')
Button_Style = collections.namedtuple('Button_Style', 'color border label')

button = Button_Style(Colors.silver,
                      Button_Border(Colors.black, 2),
                      Button_Label(Colors.black, "Arial", 15))



