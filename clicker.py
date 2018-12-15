from pykeyboard import PyKeyboard
import sys

class Clicker():
	def __init__(self):
		self.keyboard = PyKeyboard()

	def input(self, s):
		self.keyboard.type_string(s)

	def delete(self, l = 1):
		if (sys.platform == "darwin"):
			self.keyboard.tap_key('delete', n = l)
		elif (sys.platform == "win32"):
			self.keyboard.tap_key(self.keyboard.backspace_key, n = l)

	def newline(self):
		if (sys.platform == "darwin"):
			self.keyboard.tap_key('return')
		elif (sys.platform == "win32"):
			self.keyboard.tap_key(self.keyboard.return_key)
