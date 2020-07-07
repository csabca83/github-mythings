class Value:
    variable=5
    def __init__(self,age):
        self.age=age
        if type(self.value)==str:
            print('Ez egy string')
        elif type(self.value)==int:
            print('Ez egy int')
    def update(self):
        self.age=40
    def describe(self):
        print(self.age)
        print(self.variable)
value1=Value(20) #a 20at irja be a self.agere
value2=Value(30)
value1.update() # a value1et berakja a self hlyere igy lesz Value.update(value1)
value1.describe()
Value.describe(value2) #amirol szol az ezelotti komment
lst=[1,2,3,4,5]
list.append(lst,5) #list class,a method az append 
# class list,def append(self,argument)
lst.append(5) # az lst berakja a self helyere magatol,igy nekunk mar csak az argumentet kell megadni
print(lst)