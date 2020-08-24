class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('Wed')

e1.nextval = e3  #        //atiranyitom a masik instancere,tehat ez pointer mivel ramutat a a masik instancera
e3.nextval = e2
print(e1.e3.dataval) #a nextvallal atugrik a masik ertekre es mefgszerzi az adatot,tehat 