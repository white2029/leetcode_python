#
# @lc app=leetcode id=1447 lang=python3
#
# [1447] Simplified Fractions
#
# https://leetcode.com/problems/simplified-fractions/description/
#
# algorithms
# Medium (60.46%)
# Likes:    75
# Dislikes: 14
# Total Accepted:    9.6K
# Total Submissions: 16K
# Testcase Example:  '2\r'
#
# Given an integer n, return a list of all simplified fractions between 0 and 1
# (exclusive) such that the denominator is less-than-or-equal-to n. The
# fractions can be in any order.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: ["1/2"]
# Explanation: "1/2" is the only unique fraction with a denominator
# less-than-or-equal-to 2.
#
# Example 2:
#
#
# Input: n = 3
# Output: ["1/2","1/3","2/3"]
#
#
# Example 3:
#
#
# Input: n = 4
# Output: ["1/2","1/3","1/4","2/3","3/4"]
# Explanation: "2/4" is not a simplified fraction because it can be simplified
# to "1/2".
#
# Example 4:
#
#
# Input: n = 1
# Output: []
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
#
#

# @lc code=start
from functools import lru_cache
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:

        @lru_cache(None)
        def gcd(x, y):
            if x == 0:
                return y
            if x == 1:
                return 1
            d = y-x
            m = min(d, x)
            p = max(d, x)
            return gcd(m, p)

        rst = []
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if gcd(i, j) == 1:
                    rst.append("{}/{}".format(i,j))
        return rst

# @lc code=end
