#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (35.79%)
# Likes:    3302
# Dislikes: 144
# Total Accepted:    490.1K
# Total Submissions: 1.4M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        valid = -1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                valid = mid
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if valid == -1:
            return [-1, -1]
        rst = []
        low, high = 0, valid
        while low < high:
            mid = low + (high - low)//2
            val = nums[mid]
            if val == target:
                high = mid
            else:
                low = mid + 1
        rst.append(high)
        low, high = valid, len(nums) - 1
        while low < high:
            mid = low + (high - low)//2
            val = nums[mid]
            if low == mid:
                break
            if val == target:
                low = mid
            else:
                high = mid - 1
        rst.append(high if nums[high]==target else low)
        return rst

# @lc code=end
