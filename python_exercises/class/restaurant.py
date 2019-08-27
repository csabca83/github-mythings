class Restaurant:
	def __init__(self,food,rating):
		self.food=food
		self.rating=rating
	def kiiratas(self):
		print('Ez a kaja',self.food)
		print('Ez pedig a rating',self.rating)
	def open(self):
		print('A resti nyitva van!!!')
restaurant=Restaurant(food='kakashere',rating=5)
restaurant.kiiratas()
restaurant.open()
second_r=Restaurant('faszom',4)
second_r.kiiratas()
second_r.open()
third_r=Restaurant('lofasz',9)
third_r.kiiratas()
third_r.open()
