def dicti(first_name,last_name,middle_name=''):
	person={'first_name':first_name,
	'last_name':last_name,
	}
	if middle_name:
		person={'first_name':first_name,
		'last_name':last_name,
		'middle_name':middle_name}
	return person
person=dicti(last_name='Vendrics',first_name='Lajos',middle_name='God')
print(person)
