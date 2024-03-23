# https://www.youtube.com/watch?v=vzdNOK2oB2E&list=PLPe9IkX86X3y5m_MvtNu2ughxsvkqUNKr&index=4&t=352s
# m is the input and n is the average length of a string
#Time complexity: O(m * n)
from collections import defaultdict

class Solution:
    def groupAnagram(self, strs: list[str])->list[list[str]]:
        res = defaultdict(list) # mapping the charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1 # ord to get the ASCII value. This is done to map characters lets sa a = 0 

            res[tuple(count)].append(s) #tuple is non mutable

        return res.values()
    
instance = Solution()
strs = ["ate", "tea", "tae", "yes", "sey"]

print(instance.groupAnagram(strs))
    
