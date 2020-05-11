class Userdatabese():
	def __init__(self):
		self.name=''
		self.message=''
	def describe(self):
		admin=Admin()
		user=User()
		moderator=Moderator()
		self.name=input('Milyen pozicioban van az oldalon?')
		if self.name=='admin':
			admin.describe()
		elif self.name=='moderator':
			moderator.describe()
		elif self.name=='user':			
			user.describe()
class Admin(Userdatabese):
	def __init__(self):                 #ha nem akkarsz,atmasolni funkciokat nem kell,masolnod.Igy megkonnyited magadnak a programozast.
		self.message='Szoszi admin'     #inheritance,es masolas nelkul is megtudod valtoztatni a default attributetot.
	def describe(self):
		print(self.message)
class Moderator(Userdatabese):
	def __init__(self):
		self.message='Szoszi moderator'
	def describe(self):
		print(self.message)
class User(Userdatabese):
	def __init__(self):
		self.message='hess picsaba'
	def describe(self):
		print(self.message)
