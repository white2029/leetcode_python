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
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            return s == ''
        if s == '':
            i = 0
            while i<len(p) and p[i] == '*':
                i += 1
            return i == len(p)
        if p == '*':
            return True
        if p[0] != '*':
            i, j = 0, 0
            while i<len(p) and j<len(s):
                if p[i] == '*':
                    break
                elif p[i] == '?' or p[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    return False
            return self.isMatch(s[i::], p[j::])
        i = 0
        q = 0
        while i < len(p) and p[i] in '*?':
            q += int(p[i] == '?')
            i += 1
        if i == len(p):
            return len(s) >= q
        j = q
        while j < len(s):
            if s[j] != p[i]:
                j += 1
                continue
            if self.isMatch(s[j::], p[i::]):
                return True
            j += 1
# @lc code=end
