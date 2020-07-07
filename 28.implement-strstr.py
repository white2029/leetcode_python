#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (34.26%)
# Likes:    1572
# Dislikes: 1902
# Total Accepted:    667.1K
# Total Submissions: 1.9M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1

# @lc code=end
