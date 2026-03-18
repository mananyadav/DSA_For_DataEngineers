class Solution:
    def mostFrequentElement(self, nums):
        hash_table = [0]* 301 # Assuming the range of numbers is 0-1000
        for num in nums:
            hash_table[num] += 1
        
        
        max_frequency = 0
        max_element = 0 
        for i in range(len(hash_table)-1):
            if hash_table[i] > max_frequency:
                max_element = i
                max_frequency = hash_table[i]
        return max_element
    
    def hashMapMostFrequentElement(self, nums):
        hash_map = {}
        max_frequency = 0
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1 

            if hash_map[num] > max_frequency:
                max_frequency = hash_map[num]
                max_element = num   
        return max_element


     
Solution_obj = Solution()
arr = [100,200,200,300,300]

print(Solution_obj.mostFrequentElement(arr))

print(Solution_obj.hashMapMostFrequentElement(arr))