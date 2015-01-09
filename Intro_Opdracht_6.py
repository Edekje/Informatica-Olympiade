# Opdracht 6
# Alle onveven getallen outputten in de range input1-input2
start = int(input())
stop = int(input())

if(start%2 != 1):
    start += 1

for i in range(start, stop+1, 2):
    print(i)
