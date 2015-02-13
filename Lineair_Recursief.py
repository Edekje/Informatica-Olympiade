# Voorbeeld van een lineair-recursieve functie
import math

def factorise(num):
    if(num == 1):
        return [1]
    if(num == 2):
        return [2]
    # 2 checken geeft de mogelijkheid om vervolgens steeds in stappen van twee de oneven getallen te bekijken
    if num % 2 == 0: 
        return factorise(int(num/2)) + [2] # Recursive call
    
    for i in range(3,int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return factorise(int(num/i))+[i] # Recursive call
    else: # Deze else is niet strikt noodzakelijk, maar als een loop zonder breaks eindigt entert hij de else
        return [int(num)]

# Voorbeelden:

print([1]+[1])

for i in range(1,101):
    print(i)
    print(factorise(i))
    
