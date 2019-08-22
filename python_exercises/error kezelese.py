while True:
	try:
		a=int(input('Add meg az elso szamot'))
		break
	except ValueError:
		print('Ez nem szam')		
while True:
	try:
		b=int(input('add meg a 2. szamot'))
		break
	except ValueError:
		print('ez nem szam okor')
