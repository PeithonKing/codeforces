x, y = [int(x) for x in input().split()]

d = (x**2+y**2)**0.5

# taking care of borders
if not x*y or not d%1:
    print("black")

# rest cases...
elif x*y>0:
    d = int(d)
    if d%2:
        print("white")
    else:
        print("black")

else:
    d = int(d)
    if d%2:
        print("black")
    else:
        print("white")