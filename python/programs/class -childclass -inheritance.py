class Location():
	def __init__(self,location):
		self.location=location
	def holvan(self):
		self.location=input('Merre is van?')
		if self.location.lower()=='dunaszerdahely':
			print('korbe megyunk a korforgalomban')
		else:
			print('ej')
class Restaurant():
	def __init__(self,name,visits,rating):
		self.name=name
		self.visits=visits
		self.rating=rating
		self.locationa=Location(7)                 #using instance as attribute,kell irni valamit a locationbe mer maskepp beriaszt,de az inputtal ezt atirjuk
 	def describe(self):
		print('Neve:',self.name)
		print('latogatok szama:',self.visits)
		print('ratingje:',self.rating)
		self.locationa.holvan()
class Icecream(Restaurant):                                      # childclass
	def __init__(self,name,visits,rating):
		super().__init__(name,visits,rating)
hettorpe=Icecream(name='hettorpe',visits=200,rating=3.6)
hettorpe.describe()
