#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (37.74%)
# Likes:    1174
# Dislikes: 53
# Total Accepted:    133.8K
# Total Submissions: 354.2K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
#
# It's guaranteed the answer fits on a 32-bit signed integer.
#
# Example 1:
#
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# Example 2:
#
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
#
#
#

# @lc code=start
from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(maxsize=None)
        def helper(si, ti):
            if si >len(s):
                return 0
            if ti == len(t):
                return 1
            if si == len(s):
                return 0
            return helper(si+1, ti) + (0 if s[si]!=t[ti] else helper(si+1, ti+1))

        return helper(0,0)

# @lc code=end
