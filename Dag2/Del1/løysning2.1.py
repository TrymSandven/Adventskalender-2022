import os
import os.path

def steinSaksPapir():
    meg = {'X':1, 'Y':2, 'Z':3}
    total = 0
    
    try:
        fila=open('./Dag2/Del1/input.txt')
    except:
        print('Kan ikkje opna filen')

    for linje in fila:
        total += meg[linje[-2]]

        if linje[0] == 'A':
            if linje[-2] == 'Y':
                total += 6
            elif linje[-2] == 'X':
                total += 3
            else:
                pass
        
        elif linje[0] == 'B':
            if linje[-2] == 'Z':
                total += 6
            elif linje[-2] == 'Y':
                total += 3
            else:
                pass
        
        elif linje[0] == 'C':
            if linje[-2] == 'X':
                total += 6
            elif linje[-2] == 'Z':
                total += 3
            else:
                pass

    print(total)

steinSaksPapir()
