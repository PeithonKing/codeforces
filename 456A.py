laptops = {}

n = int(input())

for i in range(n):
    a, b = input().split()
    laptops[int(a)] = int(b)


happy = False
for key, value in laptops.items():
    try:
        if laptops[key]>laptops[key+1]:
            happy = not happy
            break
    except: pass

if happy: print("Happy Alex")
else: print("Poor Alex")