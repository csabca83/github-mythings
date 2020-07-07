from random import *
a=[randint(1,20) for x in range(30)]
b=[int(input('nyeroszamok')) for x in range(5)]
c=[list.count(b,x) for x in b]
print(a)
print(len(c),c)