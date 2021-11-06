def primes(n):
    prime = [True]*(n+1)
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    r = []
    for p in range(2, n+1):
        if prime[p]:
            r.append(p)
    return r


def delCharN(s, c, n):
    i = 0
    while i<len(s) and n:
        if s[i] == c:
            n-= 1
            s.pop(i)
        else:
            i += 1
    return s
            
s = input()
smod = len(s)
st = set(s)

counts = {}

for c in st:
    counts[c] = s.count(c)

imp = []
pr = primes(int(smod/2))
for p in pr:
	for i in range(int(smod/p)):
		add = p*(i+1)
		if add not in imp:
			imp.append(add)
imp.sort()


imp_len = len(imp)
iit_c = None

do = False

for key, value in counts.items():
    if value >= imp_len:
        do = True
        iit_c = key
        break

if do:
    print("YES")
    sl = list(s)
    ans = [None]*smod
    for pos in imp:
        ans[pos-1] = iit_c
    sl = delCharN(sl, iit_c, imp_len)
    i = 0
    while i<len(ans):
        if not ans[i]:
            ans[i] = sl[0]
            sl.pop(0)
        i += 1
    print("".join(ans))
    
else:
    print("NO")