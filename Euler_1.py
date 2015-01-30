# Vind som van alle natuurlijke getallen onder 1000 die veelvouden zijn van 3 of 5

# Opzetten
som = 0

for i in range(1,1000):
    if(i%3 == 0 or i%5 == 0):   # Check of ze aan de voorwaarde voldoen
        som += i
print(som)
