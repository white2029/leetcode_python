#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.28%)
# Likes:    3371
# Dislikes: 1213
# Total Accepted:    368.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        last = len(nums) - 1
        while last >= 1:
            if nums[last] <= nums[last-1]:
                last -= 1
            else:
                break
        if last == 0:
            nums.sort()
            return
        next_choice = len(nums) - 1
        while next_choice >= last-1:
            if nums[next_choice] > nums[last-1]:
                break
            next_choice -= 1
        print(last, next_choice)
        nums[last-1], nums[next_choice] = nums[next_choice], nums[last-1]
        nums[last::] = reversed(nums[last::])


# @lc code=end
