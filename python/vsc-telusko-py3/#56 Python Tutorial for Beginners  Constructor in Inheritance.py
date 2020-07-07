#   if you create object of Sub class it will first try to find
#   init of Sub class,if it is not found tyhen it will call init of Super class
class Mama:
    def __init__(self):
        self.feeling=8
        self.kor=input('Mi a korod?')
        self.name=input('Mi a neved?')
        self.megiteles='oregasszony'
    def describe(self):
        print('A feeling {},a korod {}'.format(self.feeling,self.kor))
        print('Megiteles:',self.megiteles)
class Anyu(Mama):
    def __init__(self,kirandulas_hely):
        self.vakacio=self.Vaka()
        self.kirandulas_hely=kirandulas_hely     #ezek a instance variablek pluszban lesznek
        super().__init__()                       #behuzzuk a parent classbol
        self.megiteles='40es'                      #azert irjuk utana hogy ezzel atirjuk a instance variablet,elotte irnank akkor a parentos init irna at a mienket
    def describe(self):
        print('O az',self.name)
        super().describe()
    def kirandulas(self):
        print('Ide megyunk -->',self.kirandulas_hely)
        for key,value in self.vakacio.ruha.items():
            print('{} ezt fogjuk vinni {}.'.format(key,value))
        print('osz',self.vakacio.ruha)
    class Vaka:
        def __init__(self):
            self.ruha={'felso':'rovidujju','nadrag':'rovidnardrag'}
            self.cipo={'vacsorara':'szepcipo','strand':'tangapapucs'}
            self.ruha.update(self.cipo)
class Lali(Anyu):
    def __init__(self):
        super().__init__(kirandulas_hely='balaton')
        self.megiteles='okleveles'
    def describe(self):
        super().describe()
lali=Lali()
#lali.describe()
lali.kirandulas()    