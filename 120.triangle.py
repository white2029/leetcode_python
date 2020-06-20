#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (43.50%)
# Likes:    1905
# Dislikes: 230
# Total Accepted:    242.7K
# Total Submissions: 557.5K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = [0] * len(triangle[-1])
        for row in triangle[::-1]:
            prev = [prev[i] + row[i] for i in range(len(prev))]
            if len(row) == 1:
                return prev[0]
            prev = [min(prev[i], prev[i+1]) for i in range(len(prev)-1)]
        return prev[0]



# @lc code=end
