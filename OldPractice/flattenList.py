listOfList = [1,[2,3,[4,5]],6,[[7],[8,9,10]]]
#listOfList = [[1,2],[3,4]]
print(type(listOfList))
newList = []

def process(data):
    for i in data:
        if type(i) == list:
            process(i)
        else:
            newList.append(i)
    return newList

def prinList():
    for i in listOfList:
        print(i)
#prinList()
print(process(listOfList))            



