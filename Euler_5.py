"""
Uitleg vooraf van het algoritme:
Bereken de kgv van 1 en 2, dan van dat kgv en 3 etc. tm 20

Om de kgv te berekenen: neem de pfo van elk, tel die bijelkaar op als lijsten
en verwijder de doorsnede van beiden eenmaal (doorsnede=gemeenschappelijke)

Berekening doorsnede lijst1, lijst2:
Voor elk element in lijst1:
als het in lijst2 zit voeg het bij de te returnen waardes en verwijder het uit 2

Pfo is simpel: die zoekt tot de wortel
"""

import math

def doorsnede(list1, list2):
    # Creeer de lijst van het antwoord. Het is nodig nieuwe objecten te maken met
    # list() omdat we anders de waardes van list1 in het hoofdprogramma veranderen!
    returnme = []
    lijst1 = list(list1)
    lijst2 = list(list2)
    
    for i in lijst1:
        if i in lijst2:
            returnme.append(i)
            lijst2.remove(i)
    
    return returnme

def pfo(num):
    factors = []

    while num != 1:
        # Zoeken verder dan de wortel is nutteloos: dan is het priem
        maxi = int(math.sqrt(num))+1

        for i in range(2, maxi):
            if num%i == 0:
                factors.append(i)
                num /= i
                num = int(num)
                break
        else:
            # Een loop entert een else erna als er geen breaks waren
            # In dit geval is het dan dus een priem
            factors.append(num)
            num = 1

    return factors


def kgv(num1, num2):
    list1 = pfo(num1)
    list2 = pfo(num2)
    list3 = doorsnede(list1, list2)
    list4 = list1+list2
    # Verwijder de dubbele elementen in 3 dmv de doorsnede
    for i in list3:
        list4.remove(i)

    num = 1
    # Vind wat ze vermenigvuldigd met elkaar zijn
    for i in list4:
        num *= i

    return num

num = 1

# Pak de kgvs van 1-20 samen
for i in range(2, 21):
    num = kgv(num, i)
print(num)
