S='bytdag' 
a= [4,3,0,1,2,5]
msg = S[0]

i=0 
iteration=0


while a[i]!=0:
    value = a[i]
    print(f"Iteration {iteration} :{value}")
    msg+=S[value]
    print(f"msg: {msg}")
    i=value
    print(f"value of next index:{i}")
    iteration+=1

print(f"Final msg:  {msg}")

   

