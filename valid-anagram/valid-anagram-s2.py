# By sorting them
# Time complexity: It depends on the sorting algorithm 
# Bubble sort = n^2 or it can be nlogn
# Time complexity: Depends on the sorting algorithm as well
# It can be O(n) or O(1) 
# During interviews, they will just assume sorting algorithms don't take extra space

class Solution:
    def isAnagram(self, s: str, t: str)->bool:
        return sorted(s) == sorted(t)

instance = Solution()
a = "tes"
b = "sete"

print(instance.isAnagram(a, b))