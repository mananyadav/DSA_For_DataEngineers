class Solution:
    def reverse(self, arr: list, n: int) -> None:

        reversed_array = []
        for i in range(n):
            reversed_array.append(arr[n - i - 1 ])

        return reversed_array
    

Solution_obj = Solution()
arr = [1, 2, 3, 4, 5]
result = Solution_obj.reverse(arr, len(arr))
print(result)