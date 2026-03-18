class Solution:
    def frequencySort(self, s):
        #your code goes here
        sdict = {}
        for i in s:
            if i in sdict:
                sdict[i] += 1
            else:
                sdict[i] = 1
        print("Presenting sdict",sdict)
        sorted_dict = [key for key,value in sorted(sdict.items(),key= lambda kv : (-kv[1],kv[0]))]
        return sorted_dict

solutions = Solution()
print(solutions.frequencySort("bbbccddaa"))