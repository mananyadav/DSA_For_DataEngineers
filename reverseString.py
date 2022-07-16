testString = "Tell me today's date"
TempString = testString
revString = ""
strLen = len(testString) -1 
num = 0
################# Method1: ################

def stringLen():
    print(len(testString))

for i in testString:
    revString += testString[strLen-num]
    num+=1
print(revString)

