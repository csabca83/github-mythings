class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer=0
	def get_descriptive_name(self):
		full_name=self.make+' '+self.model+' '+self.year
		return full_name
	def r_odometer(self):
		print(self.odometer)
	def update(self,new_odometer):
		if new_odometer>self.odometer:
			self.odometer=new_odometer
		else:
			print('kapd be a faszomat ember')
	def increaseodometer(self,number):
		self.odometer+=number
car=Car(make='2004',model='3as model',year='2015')
car.update(30)
car.increaseodometer(20)
car.r_odometer()
