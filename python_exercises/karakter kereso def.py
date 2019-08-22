def karakter(szo,betu):
	s=0
	for value in szo:
		if value==betu:
			s+=1
	print('Ennyi van benne kisgyerek:',s)

karakter(szo='csabi csabi csabi kakalna',betu='a')
