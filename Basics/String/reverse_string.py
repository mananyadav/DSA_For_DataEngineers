class Solution: 
    def reverseString(self, s):
        input_stack = []
        result = []

        for i in s:
            input_stack.append(i)
        
        while input_stack:
            result.append(input_stack.pop())
            
        return "".join(result)

    def reverseStringTwoPointer(self,s):


        lst = list(s)

        new_list = []

        
        start=0 


        end=len(s)-1
        

        while start < end:

            lst[start], lst[end] = lst[end], lst[start]
            start+=1
            end-=1
        return "".join(lst)

        return lst


solutions = Solution()
# print(solutions.reverseString("Harendra"))

print(solutions.reverseStringTwoPointer("Harendra"))