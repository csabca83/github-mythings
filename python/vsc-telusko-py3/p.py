class Szukseges:
    message='Ez a fo class'
    def __init__(self):
        self.szukseges_dolgok=['toltarto','buksza']
        self.isk=self.Iskola()
    def kiiratas(self):
        print('ami kell',self.szukseges_dolgok)
        print('ami a sulihoz kell pluszba',self.isk.plusz)
    @classmethod
    def describer(cls):
        print(cls.message)
    class Iskola:
        plusz='faszom'
Szukseges.describer()
suli=Szukseges()
suli.kiiratas()
        