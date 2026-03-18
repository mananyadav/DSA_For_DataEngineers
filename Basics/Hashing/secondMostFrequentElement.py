class Solution:
    def secondMostFrequentElement(self, nums):
        hash_map = {}

        highest_freq = -1
        second_highest_freq = -1

        highest_element = -1
        second_highest_element = -1

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        print(hash_map)
        for num in hash_map:
            if hash_map[num] > highest_freq:

                second_highest_freq = highest_freq
                second_highest_element = highest_element

                highest_freq = hash_map[num]
                highest_element = num
                # print(f"For the number : {num} , second_highest_freq :{second_highest_freq}, highest_freq : {highest_freq} ,second_highest_element : {second_highest_element}, highest_element : {highest_element}")
            elif hash_map[num] == highest_freq and num < highest_element:
                highest_freq = hash_map[num]
                highest_element = num
                # print(f"For the number : {num}, second_highest_freq :{second_highest_freq}, highest_freq : {highest_freq}, second_highest_element : {second_highest_element}, highest_element : {highest_element}") 
            elif hash_map[num] > second_highest_freq and hash_map[num] != highest_freq:
                second_highest_freq = hash_map[num]
                second_highest_element = num
                # print(f"For the number : {num} , second_highest_freq :{second_highest_freq}, highest_freq : {highest_freq} ,second_highest_element : {second_highest_element}, highest_element : {highest_element}")

            elif hash_map[num] == second_highest_freq and num < second_highest_element:
                second_highest_freq = hash_map[num]
                second_highest_element = num
        # print(hash_map)
        return second_highest_element

SolutionInstance = Solution()
print(SolutionInstance.secondMostFrequentElement([7350, 7548, 2648, 331, 3936, 4277, 9142, 1472, 7722, 3542, 3348, 5998, 6644, 7720, 5228, 1937, 3864, 2739, 3357, 2469, 6613, 9925, 6288, 5380, 1958, 1058, 4239, 3297, 5592, 2269, 8957, 5628, 4271, 3967, 4029, 9424, 8054, 7914, 722, 2438, 28, 2396, 3949, 8115, 3982, 4618, 2974, 8843, 4656, 683, 5355, 9263, 4736, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))     
        

