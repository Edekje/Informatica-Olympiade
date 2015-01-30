# Vind grootste priemfactor van 600851475143
import math

factoren = []

num = 600851475143

while(num > 1):
    for i in range(1, int(math.sqrt(num))+1, 2): # Neem stappen van twee, factors zijn nooit > sqrt
        if(num % i == 0):
            factoren.append(i)
            num /= i
print(factoren)
print(max(factoren)) # Deze functie geeft de grootste factor
