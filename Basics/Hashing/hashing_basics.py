arr = [5,6,5,6,5,7]
hash_table = [0] *10

for num in arr:
    hash_table[num]+=1

print(f"Count of 6 are : {hash_table[6]}")