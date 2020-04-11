class User():
	def __init__(self,first_name,last_name):
		self.first_name=first_name
		self.last_name=last_name
	def describe_user(self):
		print('first_name:',self.first_name.title())
		print('last_name:',self.last_name.title())
	def greet_user(self):
		print('Welcome '+self.first_name.title()+' '+self.last_name.title())
user1=User(first_name='lali',last_name='vendrics')
user1.describe_user()
user1.greet_user()
