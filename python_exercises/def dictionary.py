def build_person(first_name,last_name,location='udvarnok'):
	person={'first':first_name.title(),
	'last':last_name.title(),
	'loca':location.title()}
	return person
person=build_person('lali','vendrics')
for pers in person.items():
	print(pers)
