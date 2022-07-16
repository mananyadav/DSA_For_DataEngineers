def fn_inv(lst,l):
    cnt = 0
    for i in range(l):
        for j in range(i+1,l):
            if lst[i]> lst[j]:
                cnt+=1
    return cnt
        


if __name__ == "__main__":
    lst =[3,1,2]
    l = len(lst)
    cnt = fn_inv(lst,l)
    print(cnt)