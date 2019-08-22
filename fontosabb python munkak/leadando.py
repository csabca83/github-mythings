from random import*
from tkinter import*
ablak=Tk()
ablak.configure(background='grey')
bevitel1=Entry(ablak)
bevitel2=Entry(ablak)
bevitel3=Entry(ablak)
bevitel4=Entry(ablak)
bevitel5=Entry(ablak)
def szamitas():
        szamok=[]
        c=0
        d=0
        e=0
        f=0
        q=0    
        eltalalt=0
        lotto1=bevitel1.get()
        lotto2=bevitel2.get()
        lotto3=bevitel3.get()
        lotto4=bevitel4.get()
        lotto5=bevitel5.get()
        lotto1=int(lotto1)
        lotto2=int(lotto2)
        lotto3=int(lotto3)
        lotto4=int(lotto4)
        lotto5=int(lotto5)
        for x in range(5):
                szamok.append(randint(1,91))
        for i in range (len(szamok)):
                if szamok[c]==lotto1:
                        eltalalt=eltalalt+1       
                c=c+1
        for i in range (len(szamok)):
                if szamok[d]==lotto2:
                        eltalalt=eltalalt+1           
                d=d+1
        for i in range (len(szamok)):
                if szamok[e]==lotto3:
                        eltalalt=eltalalt+1      
                e=e+1
        for i in range (len(szamok)):
                if szamok[f]==lotto4:
                        eltalalt=eltalalt+1      
                f=f+1
        for i in range (len(szamok)):
                if szamok[q]==lotto5:
                        eltalalt=eltalalt+1
                q=q+1
        if eltalalt==0:
                cimke9.config(text='0€ ')
        if eltalalt==1:
                cimke9.config(text='0€ ')
        if eltalalt==2:
                cimke9.config(text='5€ ')
        if eltalalt==3:
                cimke9.config(text='60€ ')
        if eltalalt==4:
                cimke9.config(text='5.000€ ')
        if eltalalt==5:
                cimke9.config(text='2.000.000€ ')
        cimke7.config(text=eltalalt)
        cimke8.config(text=szamok)
        del(szamok)
cimke=Label(ablak,text='Ötös lottó')
cimke1=Label(ablak,text='Írja be a 1. számot:')
cimke2=Label(ablak,text='Írja be a 2. számot:')
cimke3=Label(ablak,text='Írja be a 3. számot:')
cimke4=Label(ablak,text='Írja be a 4. számot:')
cimke5=Label(ablak,text='Írja be a 5. számot:')
cimke6=Label(ablak,text='Ennyi számot talált el:')
cimke7=Label(ablak,text='')
cimke8=Label(ablak,text='',fg='blue')
cimke9=Label(ablak,text='')
cimke10=Label(ablak,text='Nyerőszámok:')
cimke11=Label(ablak,text='Nyereménye:')
gomb3=Button(ablak,text='Ellenőrzés',fg='green',command=szamitas)        
gomb4=Button(ablak,text='Kilépés',command=ablak.destroy,fg='darkred')
cimke.grid(row=0,column=1)
cimke1.grid(row=1,column=0)
bevitel1.grid(row=1,column=2)
cimke2.grid(row=2,column=0)
bevitel2.grid(row=2,column=2)
cimke3.grid(row=3,column=0)
bevitel3.grid(row=3,column=2)
cimke4.grid(row=4,column=0)
bevitel4.grid(row=4,column=2)
cimke5.grid(row=5,column=0)
bevitel5.grid(row=5,column=2)
gomb3.grid(row=6,column=1)
cimke10.grid(row=7,column=0)
cimke8.grid(row=7,column=2)
cimke6.grid(row=8,column=0)
cimke7.grid(row=8,column=2)
cimke11.grid(row=9,column=0)
cimke9.grid(row=9,column=2)
gomb4.grid(row=10,column=1)
cimke.configure(background='darkgreen')
cimke1.configure(background='red')
cimke2.configure(background='red')
cimke3.configure(background='red')
cimke4.configure(background='red')
cimke5.configure(background='red')
cimke6.configure(background='red')
cimke7.configure(background='white')
cimke8.configure(background='white')
cimke9.configure(background='white')
cimke10.configure(background='red')
cimke11.configure(background='red')
ablak.mainloop()
