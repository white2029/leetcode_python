#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (40.48%)
# Likes:    828
# Dislikes: 207
# Total Accepted:    174.7K
# Total Submissions: 431.5K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Example 1:
#
#
# Input: [1,3,5]
# Output: 1
#
# Example 2:
#
#
# Input: [2,2,2,0,1]
# Output: 0
#
# Note:
#
#
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
#
#
#

# @lc code=start
class Solution:
    def findMin(self, nums) -> int:
        sm = nums[0]

        # find max converges toward l
        lth = len(nums)
        l, r = 0, lth-1
        while l<r:
            while l<lth-1 and nums[l] == nums[l+1]:
                l += 1
            while r>0 and nums[r] == nums[r-1]:
                r -= 1
            if l >= r:
                break
            m = r - (r-l)//2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m - 1
        while l<lth-1 and nums[l] == nums[l+1]:
            l += 1
        print(l, nums[l])
        if l+1 < lth:
            return min(sm, nums[l+1])
        else:
            return sm


# @lc code=end
