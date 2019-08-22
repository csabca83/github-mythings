f_2018=['dsa','sa','sda','ad','asd']
f_2019=[]
def items(f_2018,f_2019):
	while f_2018:
		a=f_2018.pop()
		f_2019.append(a)
def kiiratas(f_2019):
	for x in f_2019:
		print(x)
items(f_2018,f_2019)
kiiratas(f_2019)
print(f_2018)
print(f_2019)
