#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (44.71%)
# Likes:    1977
# Dislikes: 227
# Total Accepted:    427.8K
# Total Submissions: 956.8K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        sm = nums[0]
        l, r = 0, len(nums)-1
        # find max and converge towards l
        while l < r:
            m = r - (r-l)//2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m - 1
        if l+1 < len(nums):
            return min(sm, nums[l+1])
        else:
            return sm


# @lc code=end
