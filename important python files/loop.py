lista1=[]
lista2=[]
dic={'ship':{'oriasi':'nagy'},
	'faszom':{'azis':'nagy'}}
lista2=[dic]
lista1=[lista2]
for value in lista1:
	for x in value:
		for key,value in x.items():
			for key1,value1 in value.items():
				print('Key1',key1)
				print('value1',value1)
