#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (43.06%)
# Likes:    1641
# Dislikes: 2012
# Total Accepted:    352.8K
# Total Submissions: 819.4K
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and
# return its index.
#
# The array may contain multiple peaks, in that case return the index to any
# one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
#
# Example 2:
#
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2,
# or index number 5 where the peak element is 6.
#
#
# Follow up: Your solution should be in logarithmic complexity.
#
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def helper(l, r):
            if r == l:
                return l
            if l + 1 == r:
                return l if nums[l] > nums[r] else r
            m = l + (r-l)//2
            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m
            if nums[m] < nums[m+1]:
                return helper(m+1, r)
            else:
                return helper(l, m)
        return helper(0, len(nums)-1)


# @lc code=end
