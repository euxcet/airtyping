from pykeyboard import PyKeyboard

class Clicker():
	def __init__(self):
		self.keyboard = PyKeyboard()

	def input(self, s):
		self.keyboard.type_string(s)

	def delete(self, l = 1):
		self.keyboard.tap_key('delete', n = l)

	def newline(self):
		self.keyboard.tap_key('return')
