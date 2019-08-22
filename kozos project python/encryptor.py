password=[]
filename=open('faszom.txt','r')
string=filename.read()
for x in string:
	if x=='a':
		password.append('1010101')
	elif x=='b':
		password.append('1011110')
	elif x==' ':
		password.append('0100101')
print(password)
password_string='\n'.join(password)
print(password_string)

