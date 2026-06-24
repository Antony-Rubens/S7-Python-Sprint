class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True

# --- How to run it correctly ---
s = "racecar"
t = "carrace"

# 1. Create an instance of the Solution class
solution = Solution()

# 2. Call the method on that instance and print the result
print(solution.isAnagram(s, t))  # This will output: True