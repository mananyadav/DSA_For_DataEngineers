
#Method 1 
# Time Complexity: O(n*n)
#Space Complexity: O(1)

def ngt(lst,l):
    newlst = []
    for i in range(l):
        next = -1
        for j in range(i+1,l):
            if lst[j]> lst[i]:
                next = lst[j]
                break
        print(f"Next greater element for {lst[i]} --> {next}")

if __name__ == "__main__":
    lst = [13,7,6,12]
    l= len(lst)
    ngt(lst,l)


            

