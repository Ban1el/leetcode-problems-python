#using hashmap
#O(n) - time / O(S+T)
#O(n) - space / O(S+T)
#Problem with this solution is that it needs extra memory
#Solution 2 solves the memory problem 
#Iterate one hashmap then compare to the other hashmap

class Solution:
    def isAnagram(self, s: str, t: str)->bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            print("Count S: " + str(countS[s[i]]) + " Count T: " + str(countT[t[i]]))
            
        print("")    
        for c in countS:
            print("Counts: " + str(countT.get(c, 0)))
            if countS[c] != countT.get(c, 0):
                return False
        return True
    

instance = Solution()
word1 = "yyes"
word2 = "ysye"

print(instance.isAnagram(word1, word2))