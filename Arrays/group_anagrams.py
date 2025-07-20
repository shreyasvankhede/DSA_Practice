"""
Problem: Group Anagrams
LeetCode: https://leetcode.com/problems/group-anagrams/
Category: Hashing, String Manipulation
Approach:
- For each string, create a frequency count of 26 characters (a–z).
- Use the count tuple as the key in a defaultdict to group anagrams.
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # maps character count to list of anagrams
        for s in strs:
            count = [0] * 26  # count of each letter a-z
            for ch in s:
                count[ord(ch) - ord('a')] += 1  # index mapping for letters
            res[tuple(count)].append(s)  # use tuple(count) as key
        return list(res.values())


if __name__ == "__main__":
    sol = Solution()
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(input_list))
    # Expected Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
