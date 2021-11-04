def fectors(n):
    res = []
    g = 1
    while g<=n:
        if not n%g:
            res.append(g)
        g += 1
    return res

input()

a = [int(x) for x in input().split()]

m = max(a)

f = fectors(m)

for i in f:
    a.remove(i)

n = max(a)

print(m, n)