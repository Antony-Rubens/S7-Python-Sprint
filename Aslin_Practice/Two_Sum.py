from typing import List  # Don't forget to import List for type hinting!

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i            

nums = [3, 4, 6, 2]
target = 7

# FIX: Add parentheses () here to create an instance of the class
solution = Solution()

# Now this will work perfectly!
print(solution.twoSum(nums, target))  # Output: [0, 1] (because 3 + 4 = 7)