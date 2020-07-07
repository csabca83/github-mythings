class Reggel:                    #interfacet akkor hasznaljuk ha pl van egy funkcionk aminek mindegy hogy milyen instance,es csak a printben vagy a returnben ternek el,plusz a sok inheritance gabalyodashoz vezethet
    def __init__(self):
        self.message='Hello!'
    def describe(self):
        print(self.message)
        print('Joreggelt')
class Este:
    def __init__(self):
        self.message='Hello!'
    def describe(self):
        print(self.message)
        print('Joestet')
def describe(ertek):
    ertek.describe()
reggel=Reggel()
este=Este()
for x in [reggel,este]:          #mindegy melyik instance
    describe(x)




#2.pelda csak a returnokban ternek el egy kicsivel,egy fokkal jobban atlathatobb
class Insurance:
    def __init__(self,value):
        self.value=value
    
class HomeInsurance(Insurance):     #itt az utolso ketto class interface,akkor lesz interface ha a variablek es a methodok nem ternek el
    def get_rate(self):
        return self.value**2
class CarInsurance(Insurance):
    def get_rate(self):
        return self.value**3
def printer(y):
    print(y.get_rate())
home=HomeInsurance(value=56)
car=CarInsurance(value=56)
for x in[home,car]:  #itt is mindegy melyik instancet hasznaljuk
    printer(x)