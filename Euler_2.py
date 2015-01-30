# Vind de som van alle fibonacci getallen < 4000000
# derde = tweede + eerste

eerste = 1
tweede = 2
derde = 0
som = 2 # 2 zou anders niet behandeld worden

while(derde < 4000000):
    derde = tweede + eerste
    eerste = tweede
    tweede = derde
    if(tweede % 2 == 0):
        som += tweede

print(som)
