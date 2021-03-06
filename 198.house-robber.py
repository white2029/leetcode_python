#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.84%)
# Likes:    4626
# Dislikes: 137
# Total Accepted:    507.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

# @lc code=start
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        for _ in range(0,3):
            nums.append(0)
        l = len(nums)
        #print(nums, l)

        @lru_cache(maxsize=None)
        def helper(n):
            if n in (l-1, l-2, l-3):
                return nums[n]
            val = max(helper(n+3), helper(n+2)) + nums[n]
            #print(n, val)
            return val

        return max(helper(0), helper(1))


# @lc code=end
