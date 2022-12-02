import os
import os.path
import time

def kalorier():
    t0 = time.time()
    sumering = 0
    max_liste = []
    tre_liste = []
    
    try:
        fila=open('input.txt')
    except:
        print('Kan ikkje opna filen')


    for tall in fila:
        if tall != '\n':
            sumering += int(tall)

        else:
            max_liste.append(sumering)
            sumering = 0
    

    for i in range(0, 3):
        tre_liste.append(max(max_liste))
        max_liste.remove(max(max_liste))
    
    t1 = time.time()

    print(sum(tre_liste), 'Runtime:', str(round(t1-t0, 3))+'sec')



kalorier()