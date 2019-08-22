szo=input('Add meg a szavat\t')
a=0
b=0
c=0
faszomtudja=0
for betu in szo:
	if betu=='a':
		a+=1
	elif betu=='b':
		b+=1
	elif betu=='c':
		c+=1
	else:
		faszomtudja+=1
if a>0:
	print('Ennyi a betu van:',a)
if b>0:
	print('Ennyi b betu van:',b)
if c>0:
	print('Ennyi c betu van:',c)
if faszomtudja>0:
	print('Ezekre mar nem volt kedvem:',faszomtudja)
