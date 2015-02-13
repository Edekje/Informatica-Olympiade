# Voorbeeld vertakkende recursieve functie

# Deze geeft alle variaties uit lijst L van lengte N
# Depth First Search heet dit algoritme type, want hij 'valt' meteen de diepte in
# Voor de complexiteit geldt O(L^N)

def get_vars(L,N):
    if(N == 0):
        return [[]]
    variations = []

    sub_vars =  get_vars(L, N-1)
    for i in L:
        for j in sub_vars:
            variations.append([i]+j)

    return variations

L = [1,2,3]
N = 3

print(get_vars(L,N))
