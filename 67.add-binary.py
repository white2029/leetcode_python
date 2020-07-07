#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (43.76%)
# Likes:    1762
# Dislikes: 273
# Total Accepted:    448.2K
# Total Submissions: 1M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.
#
#
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ia, ib = len(a)-1, len(b)-1
        carry = 0
        rst = ''
        while ia >= 0 and ib >= 0:
            val = int(a[ia]) + int(b[ib]) + carry
            rst = str(val % 2) + rst
            carry = val // 2
            ia -= 1
            ib -= 1

        while ia >= 0:
            val = int(a[ia]) + carry
            rst = str(val % 2) + rst
            carry = val // 2
            ia -= 1

        while ib >= 0:
            val = int(b[ib]) + carry
            rst = str(val % 2) + rst
            carry = val // 2
            ib -= 1

        if carry > 0:
            rst = str(carry) + rst
        return rst


# @lc code=end
