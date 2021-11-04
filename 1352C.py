for _ in range(int(input())):
    n, k = input().split()
    n = int(n)
    k = int(k)
    
    q = k//(n-1)
    r = k%(n-1)

    result = q*n - 1 
    if r:
        result += r+1
    
    print(result)