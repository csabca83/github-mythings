def build_p(f_name,l_name,**userinfo):
	lali={}
	lali['first_name']=f_name
	lali['last_name']=l_name
	for key,value in userinfo.items():
		lali[key]=value
	return lali
lali=build_p('lali','abdul',haja='nincs',pinze='azsincsen',halal=True)
print(lali)
