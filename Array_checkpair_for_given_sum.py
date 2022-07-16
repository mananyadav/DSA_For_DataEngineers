'''
Input: arr[] = {0, -1, 2, -3, 1}
        x= -2
Output: Pair with a given sum -2 is (-3, 1)
'''
def calcsum(a,sum):
    pos=len(a)
    print(pos)
    for i in range(0,pos-1):
        print(f"value of i : {i}")
        for j in range(i+1,pos):
            print(f"value of i : {i} and value of j : {j}")
            if (a[i]+a[j]) == sum:
               print(f"{a[i]},{a[j]}")
    
if __name__ =="__main__":
    arr = [0, -1, 2, -3, 1]
    x = -2
    calcsum(arr,x)

