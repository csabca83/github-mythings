from datetime import datetime
class Today:
	def __init__(self,happy_factor):
		self.happy_factor=happy_factor
	def describe(self):
		print('Todays happy factor:',self.happy_factor)
		print('Today date is {}:'.format(datetime.now().date()))
class Wishes(Today):
	dic={}
	def __init__(self,name,wish):
		self.name=name
		self.wish=wish
		self.dic[self.name]=self.wish
		
	def describe(self):
		if self.dic.get(self.name)==self.wish:
			print('{} wished that {}.'.format(self.name,self.dic[self.name]))
		else:
			print('There is no name or wish')
		
		happy_f.describe()
happy_f=Today(5)
anyu=Wishes(name='Anyu',wish='funyiras')
anyu.describe()
		
