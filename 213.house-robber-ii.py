#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (36.23%)
# Likes:    1660
# Dislikes: 48
# Total Accepted:    168.6K
# Total Submissions: 465.2K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
#

# @lc code=start
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        numsx = [nums[0:-1], nums[1::]]
        print(numsx)

        @lru_cache(maxsize=None)
        def get(idx, n):
            x = numsx[idx]
            llx = len(x)
            if n >= llx:
                return 0
            if n in {llx-1, llx-2}:
                return x[n]
            return max(get(idx,n+3),get(idx, n+2)) + x[n]

        def helper(idx):
            x = numsx[idx]
            if len(x) == 0:
                return 0
            if len(x) <= 2:
                return max(x)
            return max(get(idx,0), get(idx,1))

        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return max(nums)
        return max(helper(0), helper(1))
# @lc code=end
