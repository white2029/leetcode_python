#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (45.81%)
# Likes:    2714
# Dislikes: 181
# Total Accepted:    283.6K
# Total Submissions: 615.3K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start

from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        sqr = []

        i = 1
        while True:
            sqr.append(i*i)
            if sqr[-1] > n:
                sqr.pop()
                break
            i += 1
        sqrs = set(sqr)


        @lru_cache(None)
        def get(v):
            if v in sqrs:
                return 1
            min_cnt = float('inf')
            for s in sqr:
                if v > s:
                    min_cnt = min(min_cnt, get(v-s) + 1)
            return min_cnt

        return get(n)




# @lc code=end
