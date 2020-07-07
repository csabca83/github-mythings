class OntozoError(Exception):
    motorhiba='A motor leall!'           #  amikor itt irtam a printet akkor buggos volt a kod,folyton lefutot,gondolom az exceptionben valamit bezavart
class HumidityError(OntozoError):        #  de amikor igy class variableket csinaltam,mukodik
    motorhiba='A humidity nem megfelelo!'
class FenyerossegError(OntozoError):
    motorhiba='A fenyerosseg nem megfelelo'
class Ontozo:
    def __init__(self,humidity,fenyerosseg):
        self.humidity=humidity
        self.fenyerosseg=fenyerosseg
        self.message='Minden mukodik'
    def describe(self):
        if self.humidity>=70:
            print(OntozoError.motorhiba)
            print(HumidityError.motorhiba)
            raise HumidityError
        elif self.fenyerosseg>800:
            print(OntozoError.motorhiba)
            print(FenyerossegError.motorhiba)
            raise FenyerossegError
        else:
            print(self.message)
kopmunka=Ontozo(humidity=50,fenyerosseg=7000)
kopmunka.describe()