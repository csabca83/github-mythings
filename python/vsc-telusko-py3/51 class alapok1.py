class Doggo:
    def farokhossza(self,fajta):
        self.fajta=fajta
        print('Ez egy kutya',self.fajta)
szoszi=Doggo()
kormi=Doggo()
Doggo.farokhossza(kormi,'kormos') #a self helyere irja be az objectet
szoszi.farokhossza('szoszi') #a program tudja hogy a szoszi a doggohoz tartozik,a szoszit beilleszti a selfre 