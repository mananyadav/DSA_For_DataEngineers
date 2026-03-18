friend = [{"name":"Manan","Address":"Gurgaon"},{"name":"Mayank","Address":"Noida"}]
address = {"Address":"Gurgaon"}

print(friend[0]['name'])
print(address.items())

for i in range(len(friend)):
    for j in friend[i].keys():
        print(friend[i][j])
    
   