string1 = "0214638"

length = len(string1)
lst = []

for i in range(length-1 , -1 ,-1):
	print(f"value of i: {i}")
	if int(string1[i])%2 != 0:
		lst_element = i
		print(f"Value of last element :{string1[lst_element]}")
		break

print("Last odd index:", lst_element)
i= 0
while i < lst_element and string1[i] == "0":
	i+=1

print(string1[1:lst_element+1])


