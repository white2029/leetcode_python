#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.86%)
# Likes:    2058
# Dislikes: 140
# Total Accepted:    469.4K
# Total Submissions: 1M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 =
# 2).
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
#
#
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        i, j, k = 0, 1, 2
        ln = len(nums)
        absd = float('inf')
        best = None
        pk = None
        while i < ln:
            j = i + 1
            while j < ln:
                k = ln - 1 if pk is None else pk
                while k > j:
                    diff = nums[i] + nums[j] +  nums[k] - target
                    if diff > 0:
                        pk = k
                    if abs(diff) < absd:
                        absd = abs(diff)
                        best = diff + target
                    else:
                        if diff < 0:
                            break
                    k -= 1
                j += 1
            i += 1
        return best





# @lc code=end
