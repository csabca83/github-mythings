import tkinter
def lefutas():
	kiiratando=''
	betu=bevitelomezo1.get()
	for betu1 in betu:
		if betu1=='0':
			ertek='0'
			kiiratando+=ertek
		elif betu1=='1':
			ertek='1'
			kiiratando+=ertek
		elif betu1=='3':
			ertek='11'
			kiiratando+=ertek
		elif betu1=='4':
			ertek='100'
			kiiratando+=ertek
		elif betu1=='5':
			ertek='101'
			kiiratando+=ertek
		elif betu1=='6':
			ertek='110'
			kiiratando+=ertek
		elif betu1=='7':
			ertek1='111'
			kiiratando+=ertek
		elif betu1=='8':
			ertek='1000'
			kiiratando+=ertek
		elif betu1=='9':
			ertek='1001'
			kiiratando+=ertek
		elif betu1.upper()=='A':
			ertek='1010'
			kiiratando+=ertek
		elif betu1.upper()=='B':
			ertek='1011'
			kiiratando+=ertek
		elif betu1.upper()=='C':
			ertek='1100'
			kiiratando+=ertek
		elif betu1.upper()=='D':
			ertek='1101'
			kiiratando+=ertek
		elif betu1.upper()=='E':
			ertek='1110'
			kiiratando+=ertek
		elif betu1.upper()=='F':
			ertek='1111'
			kiiratando+=ertek
	szoveg.config(text=kiiratando)
ablak=tkinter.Tk()
szoveg=tkinter.Label(ablak,text='')
bevitelomezo1=tkinter.Entry(ablak)
gomb=tkinter.Button(ablak,text='nyomd meg',command=lefutas)
szoveg2=tkinter.Label(ablak,text='binary->hexa')
szoveg2.grid(row=0,column=0)
bevitelomezo1.grid(row=1,column=0)
gomb.grid(row=3,column=0)
szoveg.grid(row=4,column=0)
ablak.mainloop()
