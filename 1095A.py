n = int(input())

s = input()

take = []

i = 0
j = 0
while True:
    i += j
    take.append(i)
    j += 1
    if i+j>=n:
        break

r = [s[p] for p in take]
print("".join(r))