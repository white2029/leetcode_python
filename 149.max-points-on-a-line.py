#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (16.84%)
# Likes:    859
# Dislikes: 1951
# Total Accepted:    155K
# Total Submissions: 917.6K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

# @lc code=start
from collections import defaultdict
from decimal import Decimal
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        p = defaultdict(set)
        s = defaultdict(int)
        if len(points) == 1:
            return 1

        for i, (x,y) in enumerate(points):
            s[(x,y)] += 1
            for m,n in points[i+1::]:
                di, dj = m-x, n-y
                if di == 0:
                    k = float('inf')
                    c = m
                else:
                    k = Decimal(dj) / Decimal(di)
                    c = Decimal(y) - k * Decimal(x)
                #print(x,y,m,n,k,c)
                p[(k, c)].add((x,y))
                p[(k, c)].add((m,n))
        #print(p)
        #print(s)
        mx = 0
        for v in p.values():
            lv = sum([s[x] for x in v])
            if lv > mx:
                mx = lv

        return max(mx, max(s.values())) if s else mx




# @lc code=end
