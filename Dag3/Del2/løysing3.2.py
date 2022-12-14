import os.path
import string
import time

def pakke_sort():
    t0 = time.time()
    verdi = dict()
    total = 0
    liste = []

#Leser inn fila      
    try:
        fila=open('./Dag3/Del2/input.txt')
    except:
        print('Kan ikkje opna filen')
 
    #Tildeler ein verdi til bokstaver a-Z frå 1-52 
    for index, letter in enumerate(string.ascii_letters):
        verdi[letter] = index + 1

#Legger heile tekstfila i ei liste og legger 3 og 3 inn i ei subliste
    for line in fila:
        line = line.strip()
        liste.append(line)
    liste = [liste[i:i+3] for i in range(0,len(liste),3)]
        
    #Tilldeler kvart element i sublistene sin eigen variabel
    for i in range(len(liste)):
        del1 = set(liste[i][0])
        del2 = set(liste[i][1])
        del3 = set(liste[i][2])
        
        #Finner felles bokstav i del1 og del2, deretter i del3
        common_characters = ''.join(set(del1).intersection(del2))
        common_characters = ''.join(set(common_characters).intersection(del3))
        total += verdi[common_characters]
    t1 = time.time()
    print(total, 'Runtime:', str(round(t1-t0, 3))+'sec')




pakke_sort()