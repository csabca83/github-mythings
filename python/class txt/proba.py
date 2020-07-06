class OtherError(Exception):
	pass
class Valami:
	def __init__(self,value):
		self.value=value
	
	def describe(self):
		print('Hi this is your value',self.value)

class Miez():
	def __init__(self,ertek):
		self.faszom=5
		self.ertek=ertek
	def what(self):
		print('Na hesse!')
class Asus():
	
	def __init__(self,product):
		self.product=product
		war=Warranty() #amikorra a program lefut mar fel fogja ismerni a classt
		if self.product.lower()=='asus':
			print('Ez egy {} product'.format(self.product))
		else:
			try:
				raise OtherError
			except OtherError:
				Miez('1').what()
				print(Miez('1').faszom) #igy betudunk hivni barmilyen attributot,methodot csak mivel lefut a class ezert a init is lefog futni ahova kell az argument
				print('ez az ertek {}'.format(Miez('1').ertek))
				doggo.describe() #amikorra az except lefut akkor mar lesz doggo instance,igy a program gond nelkul fel fogja ismerni
	def __repr__(self):                  # A __repr__ megnezni
		return 'Ez egy termek {}'.format(self.product)
class Warranty():
	def __init__(self):
		print('boo')
doggo=Valami(value='Asus')
monitor=Asus('Lenovo')
print(monitor)
