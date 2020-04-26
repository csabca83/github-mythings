class Car():
	def __init__(self,name,year):
		self.name=name
		self.year=year
		self.uzemanyag='benzin'
	def kiiratas(self):
		print('Uzemanyaga:',self.uzemanyag)
		print('ennek az eve:',self.year)
		print('A neve:',self.name)

class Electrocar(Car):
	def __init__(self,name,year):
		super().__init__(name,year)
		self.uzemanyag='villany'
	def kiiratas(self):
		print('Ez most meno')
		print('Uzemanyaga:',self.uzemanyag)
		print('ennek az eve:',self.year)
		print('A neve:',self.name)

class Diesel(Car):
	def __init__(self,name,year):
		super().__init__(name,year)
		self.uzemanyag='diesel'
	def kiiratas(self):
		print('Uzemanyaga:',self.uzemanyag)
		print('ennek az eve:',self.year)
		print('A neve:',self.name)
		print('En dieselt nem vennek')
		
benzines=Car(name='skoda',year=10)
villamos=Electrocar(name='tesla',year=2)
dieseles=Diesel(name='nemtom',year=30)


benzines.kiiratas()
villamos.kiiratas()
dieseles.kiiratas()
