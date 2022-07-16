a = [-1,5,1,2,8,3]
a.sort()

for i in a:
    if i < 0:
        if 1 not in a:
            print(1)
            break
    else:
        if i+1 not in a:
            print(i+1)
            break
    