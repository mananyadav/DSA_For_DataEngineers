class Solution:  
    def largeOddNum(self, s: str) -> str:
        length = len(s)
        lst = []

        lst_element = -1

        for i in range(length-1 , -1 ,-1):
            
            if int(s[i])%2 != 0:
                lst_element = i
                
                break

        if lst_element == -1:
            return ""
        
        i= 0
        while i < lst_element and s[i] == "0":
            i+=1

        return s[i:lst_element+1]

solutions = Solution()

print(solutions.largeOddNum("0214638"))