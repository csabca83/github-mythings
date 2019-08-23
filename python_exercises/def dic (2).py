def build_person(first_name,last_name,location='udvarnok',age=''):
	person={'first':first_name.title(),
	'last':last_name.title(),
	'loca':location.title()}
	if age:
		person['age']=age
	return person
person=build_person('lali','vendrics',)
for pers in person.items():
	print(pers)

