palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        mult = str(i*j)
        if(mult == str(mult)[::-1]):
            palindromes.append(int(mult))
print(max(palindromes))
