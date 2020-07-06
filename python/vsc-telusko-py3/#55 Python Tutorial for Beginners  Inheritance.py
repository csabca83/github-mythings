class A:
    def feature_1(self):
        print('feature_1 is working')
    def feature_2(self):
        print('feature_2 is working')
class B(A):                   #single level inheritance
    def feature_3(self):
        print('feature_3 is working')
class C(B):
    def feature_4(self):      #multi level inheritance
        print('feature_4 is working')
class D:
    def feature_5(self):
        print('feature_5 is working')
class E(D,B):                 #multiple inheritance
    def feature_6(self):
        print('feature_6 is working')
b=B()
print(E.mro())    #sorrendet nezi
