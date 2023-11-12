#designhry
from array import *
pole = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in pole:
    for j in i:
        print(j,end = " ")
    print()
    

    
#hra
hrac = 0
while hrac < 9:
    if (hrac % 2 == 0):
        x = int(input('Hráč X zadává: '))
        match x:
            case 1:
                pole[0][0] = 'X'
            case 2:
                pole[0][1] = 'X'
            case 3:
                pole[0][2] = 'X'
            case 4:
                pole[1][0] = 'X'
            case 5:
                pole[1][1] = 'X'
            case 6:
                pole[1][2] = 'X'
            case 7:
                pole[2][0] = 'X'
            case 8:
                pole[2][1] = 'X'
            case 9:
                pole[2][2] = 'X'
        for row in pole:
            for elem in row:
                print(elem, end=' ')
            print()
        hrac = hrac + 1
    elif(hrac % 2 == 1):
        x = int(input('Hráč O zadává: '))
        match x:
            case 1:
                pole[0][0] = 'O'
            case 2:
                pole[0][1] = 'O'
            case 3:
                pole[0][2] = 'O'
            case 4:
                pole[1][0] = 'O'
            case 5:
                pole[1][1] = 'O'
            case 6:
                pole[1][2] = 'O'
            case 7:
                pole[2][0] = 'O'
            case 8:
                pole[2][1] = 'O'
            case 9:
                pole[2][2] = 'O'
        for row in pole:
            for elem in row:
                print(elem, end=' ')
            print()
        hrac = hrac + 1
    if(pole[0][0] == pole[0][1] == pole[0][2] or
        pole[1][0] == pole[1][1] == pole[1][2] or
        pole[2][0] == pole[2][1] == pole[2][2] or
        pole[0][0] == pole[1][0] == pole[2][0] or
        pole[0][1] == pole[1][1] == pole[2][1] or
        pole[0][2] == pole[1][2] == pole[2][2] or
        pole[0][0] == pole[1][1] == pole[2][2] or
        pole[2][0] == pole[1][1] == pole[0][2]):
            if(hrac % 2 == 0):
                print('Hráč O vyhrál!')
                break
            elif(hrac % 2 == 1):
                print('Hráč X vyhrál!')
                break 
    if hrac == 9:
        print('Remíza')


