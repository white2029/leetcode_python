#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (46.39%)
# Likes:    1610
# Dislikes: 68
# Total Accepted:    276.5K
# Total Submissions: 592.9K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ss = sorted(nums)

        def sub(i):
            if i >= len(ss):
                return [[]]

            j = i
            while j < len(ss) and ss[i] == ss[j]:
                j += 1

            rst = []
            val = sub(j)
            for ii in range(0, j-i+1):
                rst += [ [ss[i]]*ii + x for x in val]
            return rst
        return sub(0)





# @lc code=end
