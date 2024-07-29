from math import isqrt, gcd

def count_pairs(x, y):
    if y % x != 0:
        return 0
    
    k = y // x
    count = 0

    for i in range(1, isqrt(k) + 1):
        if k % i == 0:
            d1 = i
            d2 = k // i
            if gcd(d1, d2) == 1:
                if d1 == d2:
                    count += 1
                else:
                    count += 2
    return count

x, y = map(int, input().split())
print(count_pairs(x,y))


