#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (33.46%)
# Likes:    1718
# Dislikes: 782
# Total Accepted:    292.2K
# Total Submissions: 869.6K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Example 1:
#
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
#
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Note:
#
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#
#
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add(n1, n2):
            i, j = len(n1)-1, len(n2)-1

            rst = ""
            carry = 0

            while i>=0 and j>=0:
                val = int(n1[i]) + int(n2[j]) + carry
                rst += str(val % 10)
                carry = val // 10
                i -= 1
                j -= 1

            while i >= 0:
                val = int(n1[i]) + carry
                rst += str(val % 10)
                carry = val // 10
                i -= 1

            while j>=0:
                val = int(n2[j]) + carry
                rst += str(val % 10)
                carry = val // 10
                j -= 1

            if carry > 0:
                rst += str(carry)
            return rst[::-1]

        def mult(n1, d):
            carry = 0
            rst = ""
            for v in reversed(n1):
                val = d * int(v) + carry
                rst += str(val % 10)
                carry = val // 10
            if carry > 0:
                rst += str(carry)
            return rst[::-1]

        rst = ""
        dlt = len(num1)
        for i, v in enumerate(num1):
            d = int(v)
            m = mult(num2, d)
            m += '0' * (dlt - 1 - i)
            rst = add(rst, m)
        rst = rst.lstrip('0')
        return rst if rst else '0'




# @lc code=end
