from string import ascii_lowercase as u

def f(s, c):
    i = 0
    while i<len(s):
        if s[i] == c:
            return s[:i] + s[i+1:]
        i += 1



t = int(input())

for _ in range(t):
    s = input()
    for char in u:
        if char in s:
            s = f(s, char)
            print(char, s)
            break