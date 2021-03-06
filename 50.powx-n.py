#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (29.55%)
# Likes:    1420
# Dislikes: 2949
# Total Accepted:    457K
# Total Submissions: 1.5M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
#

# @lc code=start
from functools import lru_cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0/self.get_n(x, -n)
        else:
            return self.get_n(x, n)
    
    @lru_cache(maxsize=None)
    def get_n(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x * x
        half_n = n//2
        val = self.get_n(x, half_n)
        if n%2 == 0:
            return val * val
        else:
            return val * val * x
            

# @lc code=end
