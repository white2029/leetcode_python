#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (60.11%)
# Likes:    2509
# Dislikes: 110
# Total Accepted:    179.2K
# Total Submissions: 298K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
#
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
#
# Example 1:
#
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#
#
# Example 2:
#
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
#
# Note:
#
#
# The input string length won't exceed 1000.
#
#
#
#

# @lc code=start
from functools import lru_cache
class Solution:
    def countSubstrings(self, s: str) -> int:
        check = dict()
        
        for i in range(0, len(s)):
            for j in range(i+1, len(s)):
                check[(i,j)] = s[i] == s[j]

        @lru_cache(maxsize=None)
        def isp(b, e):
            if b == e:
                return True
            if b+1 == e:
                return check[(b,e)]
            else:
                return check[(b,e)] and isp(b+1, e-1)

        cnt = len(s)
        for i in range(2, len(s)+1):
            for j in range(0, len(s)-i+1):
                cnt += isp(j, j+i-1)
        return cnt

# @lc code=end
