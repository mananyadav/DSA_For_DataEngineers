exp = "Manan visited IIIT"

################# Method 1######################
cmpString = ""

for i in exp:
    if i not in cmpString:
        cmpString+= i

print(cmpString)

#Time Complexity = O(n*n)
#Space Complexity = 1

################# Method 2######################
stringSet = set()
FinalString = ""
for i in exp:
    stringSet.add(i)
print(stringSet)

for i in stringSet:
    FinalString+=i

print(FinalString)

#Time Complexity = O(n)
#Space Complexity = O(n)






