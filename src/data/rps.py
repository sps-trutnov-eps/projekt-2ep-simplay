#KAMENNUZKYPAPIR
print("Kámen, nůžky a papír")
import random
first = str(input("Zadejte Kámen, Nůžky nebo Papír: "))
second = random.randint(1,3)

#CISLA
if second == 1:
    second = "Kámen"
elif second == 2:
    second = "Nůžky"
elif second == 3:
    second = "Papír"
    
#UKAŽVSTUPY
print("Zahrál jste:", first)
print("Soupeř zahrál:", second)

#REMIZA
#1-KAMEN
if first == "Kámen" and second == "Kámen":
    print("Remíza.")
#2-NUZKY
elif first == "Nůžky" and second == "Nůžky":
    print("Remíza.")
#3-PAPIR
elif first == "Papír" and second == "Papír":
    print("Remíza.")

#VYHRY
if first == "Kámen" and second == "Nůžky":
    print("Výhra, kámen drtí nůžky.")
elif first == "Kámen" and second == "Papír":
    print("Prohra, kámen je zabalen papírem.")
elif first == "Nůžky" and second == "Kámen":
    print("Prohra, nůžky jsou rozdrceny kamenem.")
elif first == "Nůžky" and second == "Papír":
    print("Výhra, nůžky stříhají papír.")
elif first == "Papír" and second == "Kámen":
    print("Výhra, papír balí kámen.")
elif first == "Papír" and second == "Nůžky":
    print("Prohra, papír je rozstřižen nůžkami.")


