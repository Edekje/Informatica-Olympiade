som = 0
som_kwadraten = 0

for i in range(1, 101):
    som += i
    som_kwadraten += i*i

print(som*som-som_kwadraten)
