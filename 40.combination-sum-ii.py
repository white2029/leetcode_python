#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (47.25%)
# Likes:    1717
# Dislikes: 65
# Total Accepted:    323.6K
# Total Submissions: 680.3K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
#
#
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        vals = sorted(candidates)
        rst = []

        def recur(i, curr):
            ttl = sum(curr)
            if ttl == target:
                rst.append(curr)
                return
            if i >= len(vals):
                return
            item = vals[i]
            if item > target:
                return
            j = i + 1
            while j<len(vals) and vals[j] == item:
                j += 1
            for x in range(0, j-i+1):
                if ttl + x*item > target:
                    break
                recur(j, curr + [item] * x)

        recur(0, [])
        return rst

# @lc code=end
