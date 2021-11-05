for _ in range(int(input())):
    input()
    a = [int(x) for x in input().split()]
    i = 1
    product = 0
    while i<len(a):
        p = a[i]*a[i-1]
        if p > product: product = p
        i+=1
    print(product)