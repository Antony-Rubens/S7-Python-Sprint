from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

sol = Solution()
print(sol.groupAnagrams(["eat", "ate", "nat", "tea", "tan", "bat"]))