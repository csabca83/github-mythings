import time
print('Sry guys,but we run out of pastrami')
sandwich_orders=[ 'pastrami','szalonnas','pastrami','paprikas','retkes','pastrami']
ready_sandwich=[]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    ready_sandwich.append(current_sandwich)
    print('Elkeszult ez a szendvics:',current_sandwich)
    time.sleep(2)
print('Az osszes szendwich elkeszult')
for key in ready_sandwich:
    print('\t',key)
