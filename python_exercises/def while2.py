lista=[]
def make_name(f_name,l_name):
	full_name=f_name+' '+l_name
	return full_name
while True:
	f_name=input('f_name')
	if f_name=='q':
		break
	l_name=input('l_name')
	full_name=make_name(f_name,l_name)
	lista.append(full_name)
for value in lista:
	print(value)
