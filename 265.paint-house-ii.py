#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#
# https://leetcode.com/problems/paint-house-ii/description/
#
# algorithms
# Hard (44.34%)
# Likes:    505
# Dislikes: 18
# Total Accepted:    58.8K
# Total Submissions: 132.5K
# Testcase Example:  '[[1,5,3],[2,9,4]]'
#
# There are a row of n houses, each house can be painted with one of the k
# colors. The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the
# same color.
#
# The cost of painting each house with a certain color is represented by a n x
# k cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color 0; costs[1][2] is the cost of painting house 1 with color 2, and so
# on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Example:
#
#
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum
# cost: 1 + 4 = 5;
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 +
# 2 = 5.
#
#
# Follow up:
# Could you solve it in O(nk) runtime?
#
#

# @lc code=start


from functools import lru_cache
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        nh = len(costs)
        nk = len(costs[0])
        cs = set(range(0, nk))

        @lru_cache(maxsize=None)
        def helper(n, c):
            if n == nh - 1:
                return costs[n][c]
            return min(
                [helper(n+1, x) for x in cs if x !=c]
            ) + costs[n][c]
        return min([helper(0, i) for i in cs])
# @lc code=end
