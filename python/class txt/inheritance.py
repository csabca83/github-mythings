class Parent:
	def __init__(self,valami):
		self.v=valami
class Child(Parent):
	def describe(self):
		print(self.v)
o=Child(valami='asd')
o.describe()
