from math import gcd
n = int(input())

a = [int(k) for k in input().split()]

i = 0

p = 0

while i < n:
    j = 0
    while j < n:
        print(f"i = {i}, j = {j}")
        x = gcd(a[i], a[j])*gcd(i, j)
        p += x
        print("\t", x)
        j += 1
    i += 1

print(p)