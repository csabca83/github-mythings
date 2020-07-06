class Valami:
    ertek=5
    def __init__(self,name):
        self.name=name
    @classmethod
    def miazertek(cls):     # ugyanugy mukodik mint a self,csak ez classokra van,kell definialnunk hogy class method
        print(cls.ertek)
    @staticmethod           #itt pedig hogy static method
    def st():
        print('Ez egy olyan method aminek semmi koze nincs a class variablehez,vagy az instance variablehez')
v1=Valami(name='Lali')
print('{} vagy pedig {}:'.format(v1.name,Valami(name='Lali').name)) #Azert kell a masodiknal megadni a namet,mivel instance variablet akkorok kiiratni,hasznaljak ilyenkor instance methodot
# a masodiknal nincs a namere megadva semmi
Valami.miazertek()
Valami.st()