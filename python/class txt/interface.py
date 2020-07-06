def location(loc):
	print('A termek',loc)
class Keyboard:
	def __init__(self):
		self.location=location(loc='pozsonyi') # betudunk hivni funkciokat es kulso classokat is,mindegy a self. utan hogyan nevezzuk el pl lehet self.whatewer=location()
class Mouse:
	def __init__(self):
		self.location=location(loc='pozsonyi')
eger=Keyboard()
