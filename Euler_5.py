# Smart solution: bereken de kgv van 1-10 samen
import math
def get_factors(num):
    factors = []
    while num != 1:
        max = 1 + int(math.sqrt(num))
        for i in range(2,max):
            if(num % i == 0):
                factors.append(i)
                num = int(num/i)
                break
        else:
            factors.append(num)
            break
    return factors

def kgv(list1, list2):
    list3 = list1
    for i in list1:
        print(i)
        try:
            list2.remove(i)
        except:
            list3.append(i)
    return list3

first = get_factors(27)
second = get_factors(33)

print(kgv(first,second))
