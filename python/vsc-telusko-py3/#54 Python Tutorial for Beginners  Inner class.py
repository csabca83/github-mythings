class Student:                   #outer class
    def __init__(self,name,rollno):
         self.name=name
         self.rollno=rollno
     #    self.lap=self.Laptop() Ez a nehezebb megoldashoz tartozik
        
    def show(self):
        print(self.name)
        print(self.rollno)
    #    self.lap.show -A nehezebb megoldassal
    class Laptop:               #inner class
        def __init__(self):
            self.brand='asus'
            self.cpu='intel'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=Student(name='Lali',rollno=5)
s2=Student(name='Anyu',rollno=3)
Student.show(s1)
#s1.show()
#s1.lap.show()
# lap1=s1.lap nehezebb megoldas
lap1=Student.Laptop() #konnyebb megoldas
lap1.show()
