class Solution:
    def ContainsDuplicate(self, nums: list[(int)])->bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
    
instance = Solution()
nums = []
nums.append(1)
nums.append(1)
print(instance.ContainsDuplicate(nums))