import os
import os.path

def steinSaksPapir():
    rps = {'A':1, 'B':2, 'C':3}
    total = 0
    
    try:
        fila=open('input.txt')
    except:
        print('Kan ikkje opna filen')

    for linje in fila:
        if linje[-2] == 'Y':
            total += 3
            total += rps[linje[0]]

        elif linje[-2] == 'Z':
            total += 6
            if linje[0] == 'A':
                total += rps['B']
            
            elif linje[0] == 'B':
                total += rps['C']
            
            elif linje[0] == 'C':
                total += rps['A']
        
        else:
            if linje[0] == 'A':
                total += rps['C']
            
            elif linje[0] == 'B':
                total += rps['A']
            
            elif linje[0] == 'C':
                total += rps['B']

    print(total)

steinSaksPapir()
