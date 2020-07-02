class CsaladError(Exception):
	pass
class Buli:
	lst=['icu','laci']
	def __init__(self,name):
		self.name=name
	def kivagy(self):
		for x in self.lst:
			if self.name==x:
				raise CsaladError
		print('welcome {}!'.format(self.name))
ujtag=Buli('icu')
try:
	ujtag.kivagy()
except CsaladError:
	print('ezt beszoptad')
	
	
				
		
