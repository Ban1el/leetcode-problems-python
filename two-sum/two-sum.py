# Two sum
# Algorithm: One pass concept
# value - target
# Time complexity: O(n) | Memory Complexity: O(n)
# https://www.youtube.com/watch?v=KLlXCFG5TnA

class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    
instance = Solution()
nums = [1, 2, 3, 4, 5]
print(instance.twosum(nums, 6))
