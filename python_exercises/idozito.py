from datetime import datetime
import time
kulonbseg=0
while True:
    meddig=int(input('Mennyi masodperctol szamoljak vissza?'))
    answer=input('Kezdhetem a szamolast?')
    a=datetime.now()
    a=a.timestamp()
    if answer=='igen' or answer=='ja':
        while kulonbseg!=meddig:
            b=datetime.now()
            b=b.timestamp()
            kulonbseg=b-a
            kulonbseg=round(kulonbseg,0)
            time.sleep(.5)
        print('megvagyok')
