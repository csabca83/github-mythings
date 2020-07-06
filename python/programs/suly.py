from datetime import datetime
from random import randint
class SulyError(Exception):
	pass
class Suly:
	dic={}
	def __init__(self):
		self.name=Ossz().mianeved()
		self.cel=int(input('Hany kg vagy {}?'.format(self.name)))
	def __repr__(self):
		if self.cel<=69:
			return 'Ez a suly igy nem megfelelo {}'.format(self.cel)
		else:
			return 'Ez a suly igy megfelelo {}'.format(self.cel)
			dic.update({self.name:self.cel})
class Anyu(Suly):
	def __repr__(self):
		if self.cel<=73:
			return 'Ez a suly igy nem megfelelo {}'.format(self.cel)
		else:
			return 'Ez a suly igy megfelelo {}'.format(self.cel)
class Ossz:
	def mianeved(self):
		self.name=input('Name?')
		return self.name
	def describer(self,x):
		print(x,'Ez volt a suly program')
lali=Suly()
anyu=Suly()
for x in [lali,anyu]:
	Ossz().describer(x)
