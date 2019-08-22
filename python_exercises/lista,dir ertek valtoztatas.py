def  mianeved(first_name,last_name,middle_name=''):
	if middle_name:
		full_name=first_name.title()+' '+middle_name.title()
		full_name+=' '+last_name.title()
	
	else:
		full_name=first_name.title()+' '+last_name.title()
	return full_name
full_name=mianeved(first_name='allah',last_name='akbar',middle_name='more')
print(full_name)
