filename=open('decryptor.txt','r')
string=filename.read()
lista=string.split( )
print(lista)
password=[]
for x in lista:
	print(x)
	if x=='1010101':
		password.append('a')
	elif x=='1011110':
		password.append('b')
	elif x=='0100101':
		password.append(' ')
print(password)
