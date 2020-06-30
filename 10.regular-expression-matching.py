#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (26.59%)
# Likes:    4167
# Dislikes: 691
# Total Accepted:    429.3K
# Total Submissions: 1.6M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
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
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
#
#
# Example 5:
#
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#
#
#

# @lc code=start
from functools import lru_cache

def debug(fun):
    def wrapper(*args, **kwargs):
        val = fun(*args, **kwargs)
        print(args, val)
        return val
    return wrapper

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        np = ''
        i = 0
        prev = None
        occ = dict()
        while i<len(p):
            if p[i]!='*':
                np += p[i]
                prev = p[i]
                i += 1
            else:
                while i<len(p) and p[i] == '*':
                    i += 1
                if prev:
                    occ[len(np)] = prev
                    np += '*'

        p = np
        ls = len(s)
        lp = len(p)


        @lru_cache(None)
        #@debug
        def sub(i, j):
            if i >= ls:
                if j >= lp:
                    return True
                while j+1 in occ:
                    j += 2
                return j >= lp
            if j >= lp:
                return False
            if j+1 not in occ:
                if p[j] == '.':
                    return sub(i+1, j+1)
                return p[j]==s[i] and sub(i+1, j+1)
            else:
                prev = p[j]
                if prev == '.':
                    if j+2 == lp:
                        return True
                    for x in range(i, ls+1):
                        if sub(x, j+2):
                            return True
                    return False

                if sub(i, j+2):
                    return True
                for x in range(i, ls):
                    if s[x] == prev:
                        if sub(x+1, j+2):
                            return True
                    else:
                        break
                return False
        return sub(0,0)

# @lc code=end
