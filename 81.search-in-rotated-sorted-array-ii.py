#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.96%)
# Likes:    1220
# Dislikes: 462
# Total Accepted:    232.7K
# Total Submissions: 706K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true,
# otherwise return false.
#
# Example 1:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Follow up:
#
#
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
#
#
#

# @lc code=start
class Solution:
    def search(self, nums, target: int) -> bool:
        print(nums, target)
        # find max pos
        if not nums:
            return False

        l, r = 0, len(nums) - 1
        # find pos of max value (first occ)
        while l<r:
            while l < len(nums)-1 and nums[l] == nums[l+1]:
                l += 1
            while r > 0 and nums[r] == nums[r-1]:
                r -= 1
            if l>=r:
                break

            #converge towards l, first occ of min
            m = r - (r-l)//2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m - 1

        mxp = l
        print('first mxp', mxp)
        l, r = 0, mxp
        while l<=r:
            m = l + (r-l)//2
            if nums[m] == target:
                return True
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        l, r = mxp+1, len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return True
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
        return False


# @lc code=end


if __name__ == '__main__':
    print(Solution().search([2,5,6,0,0,1,2],0))
    print(Solution().search([2,5,6,0,0,1,2],3))
    print(Solution().search([3,5,1],1))
    print(Solution().search([2,2,2,0,1],1))
    print(Solution().search([1,3,1,1,1],1))
    print(Solution().search([1,3,1,1,1],3))
    print(Solution().search([3,1,1,1],2))
