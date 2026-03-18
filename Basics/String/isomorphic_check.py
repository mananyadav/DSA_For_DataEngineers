class Solution:
    
    def isomorphicString(self, s, t):
        #your code goes here
        s_dict = {}
        t_dict = {}

        for pos , ele in enumerate(s):
            if ele not in s_dict:
                s_dict[ele] = [pos]
            else:
                s_dict[ele].append(pos)

        for pos , ele in enumerate(t):
            if ele not in t_dict:
                t_dict[ele] = [pos]
            else:
                t_dict[ele].append(pos)

        # print(f"s_dict : {s_dict} , t_dict : {t_dict}")
        s_list = [ value for value  in s_dict.values()]
        t_list = [ value for value  in t_dict.values()]

        # print(f"s_list : {s_list}, t_list : {t_list}")

        if s_list == t_list:
            return True
        else:
            return False

solutions = Solution()
print(solutions.isomorphicString("abcdabcd", "wxyzwxyz"))





