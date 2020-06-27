#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (37.94%)
# Likes:    1324
# Dislikes: 65
# Total Accepted:    91.8K
# Total Submissions: 241.7K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
#
#
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
#
#
#
# Example 2:
#
#
# Input: [1,2,4,8]
# Output: [1,2,4,8]
#
#
#
#

# @lc code=start
from functools import lru_cache
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)

        @lru_cache(None)
        def get(i):
            max_length = 0
            best = []
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    lj = get(j)
                    if len(lj) > max_length:
                        max_length = len(get(j))
                        best = lj
            return list(best) + [nums[i]]

        best = []
        for i in range(0, len(nums)):
            val = get(i)
            if len(val) > len(best):
                best = val
        return best




# @lc code=end
