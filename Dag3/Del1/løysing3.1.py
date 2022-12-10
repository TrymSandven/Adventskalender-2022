import os
import os.path
import time
import string

def pakke_sort():
    verdi = dict()
    total = 0

#Leser inn fila      
    try:
        fila=open('./Dag3/Del1/input.txt')
    except:
        print('Kan ikkje opna filen')
 
    #Tildeler ein verdi til bokstaver a-Z frå 1-52 
    for index, letter in enumerate(string.ascii_letters):
        verdi[letter] = index + 1
    
    

    #Deler opp linja i to like deler
    for line in fila:
        del1 = line[:len(line)//2]
        del2 = line[len(line)//2:]
        
        #Finner felles bokstav i dei to tekststrengene
        common_characters = ''.join(set(del1).intersection(del2))
        total += verdi[common_characters]
    print(total)




pakke_sort()