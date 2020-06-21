#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#
# https://leetcode.com/problems/paint-house/description/
#
# algorithms
# Easy (51.83%)
# Likes:    800
# Dislikes: 78
# Total Accepted:    85K
# Total Submissions: 163.9K
# Testcase Example:  '[[17,2,17],[16,16,5],[14,3,19]]'
#
# There are a row of n houses, each house can be painted with one of the three
# colors: red, blue or green. The cost of painting each house with a certain
# color is different. You have to paint all the houses such that no two
# adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x
# 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color red; costs[1][2] is the cost of painting house 1 with color green, and
# so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Example:
#
#
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2
# into blue.
# Minimum cost: 2 + 5 + 3 = 10.
#
#
#

# @lc code=start

def debug(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        #print(*args, val)
        return val
    return wrapper

from functools import lru_cache
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        nh = len(costs)

        @lru_cache(maxsize=None)
        @debug
        def get(n, c):
            if n >= nh:
                return float('inf')
            if c > 2:
                return float('inf')
            if n == nh - 1:
                return costs[n][c]
            return min(
                [get(n+1, x) for x in {0,1,2} if x != c]
            ) + costs[n][c]
        return min([get(0,0), get(0,1), get(0,2)])


# @lc code=end
