#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (24.44%)
# Likes:    1923
# Dislikes: 108
# Total Accepted:    241.7K
# Total Submissions: 986.9K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
# Example 3:
#
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
#
#
# Example 4:
#
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
#
#
# Example 5:
#
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
#
#
#

# @lc code=start
from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ls = len(s)
        lp = len(p)

        @lru_cache(None)
        def sub(i, j):
            if i >= ls:
                if j >= lp:
                    return True
                while j<lp and p[j]=='*':
                    j += 1
                return j>=lp
            if j >= lp:
                return False
            if p[j] == '?':
                return sub(i+1, j+1)
            if p[j] != '*':
                return p[j]==s[i] and sub(i+1, j+1)
            while j<lp and p[j] == '*':
                j += 1
            if j >= lp:
                return True
            if p[j] == '?':
                return any([sub(x, j) for x in range(i, ls)])
            return any([sub(x, j) for x in range(i, ls) if s[x] == p[j]])
        return sub(0,0)




# @lc code=end
