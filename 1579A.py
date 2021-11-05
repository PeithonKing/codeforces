for _ in range(int(input())):
    s = input().upper()
    A = s.count("A")
    B = s.count("B")
    C = s.count("C")
    if A+C == B: print("\tYes")
    else: print("\tNo")
