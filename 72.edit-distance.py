#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (44.06%)
# Likes:    3914
# Dislikes: 56
# Total Accepted:    278.9K
# Total Submissions: 629.4K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#

# @lc code=start
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if word1 == word2:
            return 0
        if len(word1) == 1 and len(word2) == 1:
            return 1
        w1, w2 = (word1, word2) if len(word1) >= len(word2) else (word2, word1)
        if w1[0] == w2[0]:
            return self.minDistance(w1[1::], w2[1::])
        return min([self.minDistance(w1[1::], w2[1::]),
                    self.minDistance(w1[1::], w2),
                    self.minDistance(w1, w2[1::])]) + 1

# @lc code=end
