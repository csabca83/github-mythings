class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=5
	def describe_restaurant(self):
		print('name:',self.restaurant_name)
		print('type:',self.cuisine_type)
	def open_restaurant(self):
		print(self.restaurant_name,'is now open')
	def number_serv(self,latogatok):
		self.number_served=latogatok
		print(self.number_served)
		
r=Restaurant('kissburger','hambi')
r.number_serv(10)
