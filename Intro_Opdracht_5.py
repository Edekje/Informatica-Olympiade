# Opdracht 5
# Neemt input tot 0 is geentered, dan output som

som = 0 # Alvast opzetten
invoer = 1 # Arbitraire waarde: het moet geen 0 zijn

while(invoer != 0):
    invoer = int(input())
    som += invoer
print(som)
