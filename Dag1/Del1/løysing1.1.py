import os
import os.path
import time

def kalorier():
    t0 = time.time()
    sumering = 0
    liste = []

#Leser inn fila      
    try:
        fila=open('./Dag1/Del1/input.txt')
    except:
        print('Kan ikkje opna filen')


    for tall in fila:
        if tall != '\n':
            sumering += int(tall)

        else:
            liste.append(sumering)
            sumering = 0
    t1 = time.time()
    print(max(liste), 'Runtime:', str(round(t1-t0, 3))+'sec')



kalorier()
#