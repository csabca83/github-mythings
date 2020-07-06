class Valami:
    variable=56              # class variable,class namespace
    def __init__(self,name):
        self.name=name       # instance variable,instance namespace
com1=Valami(name='lali')
print(com1.name)             # minden instancanal valtozhat
print(Valami.variable)        #minden instancenal ugyanaz  
# namespace is an area where you create and store object/variable
