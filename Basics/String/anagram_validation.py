class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here
        s_sortedlist = "".join(sorted(s.lower()))
        t_sortedlist = "".join(sorted(t.lower()))
        if s_sortedlist == t_sortedlist:
            return True
        else:
            return False

solutions = Solution()
print(solutions.anagramStrings("Hello", "World"))
        