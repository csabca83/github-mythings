class Message:
    def __init__(self,message,sender):    
        self.message=message
        self.sender=sender
class Ujtext:
    def __init__(self,utext,username):
        self.utext=utext
        self.username=username
    def describe(self,umessage):  #az umessage itt a message lesz
        if umessage.sender==self.username or self.username=='admin':  #umessage.senderrel  -megkapjuk a Message.sendert
            umessage.message=self.utext
            print('Sikeres a valtoztatas')
            print(umessage.message)
        else:
            print('Sikertelen')
message=Message('Hi','lali')
uj=Ujtext('Hello','admin')
uj.describe(message)