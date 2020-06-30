#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.74%)
# Likes:    3364
# Dislikes: 5308
# Total Accepted:    1.1M
# Total Submissions: 4.3M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
#
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        strx = str(x)[int(neg)::]
        revx = ''.join(list(reversed(strx)))
        val = int(revx) * (-1 if neg else 1)
        if not (-2**31-1 <= val <= 2**31):
            return 0
        return val

# @lc code=end
