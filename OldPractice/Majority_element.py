'''
Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater
than the half of the size of the array size. 
'''

def majority_element(arr):
    rep = {}
    length = len(arr)/2
    flag = 0
    #print(length)
    for i in arr:
        if i not in list(rep.keys()):
            rep[i] = 1
        else:
            rep[i]+=1
    for checks in rep:
        if rep[checks]>length:
            print(checks)
            flag = 1
    if flag == 0:
        print("No value found")






if __name__=="__main__":
    a = [3, 3, 4, 2, 4, 4, 2, 4]
    majority_element(a)

