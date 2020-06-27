#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (45.11%)
# Likes:    1553
# Dislikes: 220
# Total Accepted:    94K
# Total Submissions: 208.8K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all
# nodes to receive the signal? If it is impossible, return -1.
#
#
#
# Example 1:
#
#
#
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
#
#
#
#
# Note:
#
#
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
#
#
#

# @lc code=start
from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited = set()
        conn = defaultdict(dict)
        for i, j, w in times:
            conn[i][j] = w

        h = []
        if K > N:
            return -1
        if not conn[K]:
            return -1

        for v, c in conn[K].items():
            heappush(h, (c, v, K))

        cost = dict()
        cost[K] = 0

        while h:
            c, d, f = heappop(h)
            if d not in cost:
                cost[d] = c
                for v, cv in conn[d].items():
                    if v not in cost:
                        heappush(h, (c+cv, v, d))

        return max(cost.values()) if len(cost)==N else -1



# @lc code=end
