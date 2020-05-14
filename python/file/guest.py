filename='guest.txt'
string=''
with open (filename,'a') as file_object:
	pass
while True:
	guest=input('Van meg guest?')
	if guest!='n' and guest!='lista':
		guestname=input('mianeve?')
		with open(filename) as file_object:
			content=file_object.readlines()
		for x in content:
			string+=x.strip()
			string+='\n'
		if guestname in content:
			print('kerem foglaljon helyet,rajta van a listan')
		else:
			with open (filename,'a') as file_object:
				file_object.write(guestname)
				file_object.write('\n')
				print('felirtam a listara')	
	elif guest=='lista':
		print(string)
	else:
		break
