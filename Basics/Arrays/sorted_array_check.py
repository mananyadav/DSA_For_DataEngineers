class Solution:
    def arraySortedOrNot(self, arr, n):

        sorted_flag = True 

        for i in range(n - 1):
             if (arr[i+1] < arr[i]):
                    return False

        #     if (arr[i+1] < arr[i]) and (i <= n-1):
        #         return False
        return sorted_flag
    
Solution_obj = Solution()
arr = [1, 2, 3, 6, 5]

Solution_obj.arraySortedOrNot(arr, len(arr))
print(Solution_obj.arraySortedOrNot(arr, len(arr)))