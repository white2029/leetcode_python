#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (30.29%)
# Likes:    2489
# Dislikes: 132
# Total Accepted:    257.4K
# Total Submissions: 847.1K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        start = 0
        end = 1
        depth = 0
        while True:
            if end >= len(nums):
                return depth
            new_end = -float('inf')
            for i in range(start, end):
                new_end = max(new_end, nums[i] + i + 1)
            start, end = end, new_end
            depth += 1
        return -1
# @lc code=end
