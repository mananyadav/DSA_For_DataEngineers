# Print all the 
lst = ['Ram','Mohan','Manan','Manish','Mayank']

def getname(lst):
    newlst = []
    for i in lst:
        if 'Ma' in i:
            newlst.append(i)
    return newlst


val = lambda x : [i for i in x if 'Ma' in i]
print(val(lst))

print(getname(lst))


