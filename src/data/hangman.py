import random

lest = open("slova.txt", encoding = 'utf-8').read().split()
slovo = random.choice(lest)
lst = []

#pravidla hry
zivoty = 10
pocet = len(slovo)
pocet_mist = '-'
tajenka = pocet_mist * pocet
pole = list(tajenka.strip(''))

while zivoty > 0:
    i = 0
    vyhra = 0   
    while i < pocet:
        print(pole[i], end = ' ')
        if pole[i] == '-':
            vyhra = vyhra + 1
        i = i + 1       
    if vyhra == 0:
        print('')
        print('Přežil jsi!')
        break
        
    print('')
    while True:
        hadani = input('Zadejte písmenko slova: ')
        hadani = hadani.lower() 
        delka_vstupu = len(hadani)
        if delka_vstupu != 1:
            print('Zadejte PRÁVĚ jedno písmeno!')
        elif hadani.isdigit():
            print("Zadejte PÍSMENO!")
        elif hadani not in lst:
            lst.append(hadani)
            break
        else:
            print('Toto už jste zadali, zadejte něco jiného!')

    userinput = slovo.find(hadani)
    if userinput == -1:
            zivoty = zivoty - 1
            print('Toto písmeno není v daném slově, zbývá vám', zivoty, 'životů.')
            
    else:
        while userinput != -1:
            pole[userinput] = hadani
            userinput = slovo.find(hadani, userinput+1)   
        
if zivoty == 0:
    print('Byl jsi oběšen.')
    print('Slovo bylo:', slovo)
