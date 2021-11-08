from string import ascii_lowercase as l

d = {c: None for c in l}

for _ in range(int(input())):
    
    alph = input()

    for i in range(26):
        d[alph[i]] = i
    
    s = input()
    
    t = 0
    for i in range(len(s)-1):
        t += abs(d[s[i+1]]-d[s[i]])
    
    print("\t", t)
