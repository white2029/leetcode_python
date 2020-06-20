#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (54.46%)
# Likes:    1534
# Dislikes: 77
# Total Accepted:    98.9K
# Total Submissions: 181.6K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#

# @lc code=start

import functools
class Solution:
    def diffWaysToCompute(self, raw_s: str) -> List[int]:
        if not raw_s:
            return [0]
        if raw_s.startswith('-'):
            raw_s = '0' + raw_s
        vals = []
        curr = ''
        for v in raw_s:
            if v in '+-*':
                vals.append(int(curr))
                vals.append(v)
                curr = ''
            else:
                curr += v
        vals.append(int(curr))

        @functools.lru_cache(maxsize=None)
        def helper(s, e):
            if s == e:
                return [vals[s]]
            avail = []
            for i in range(s+1, e, 2):
                p1 = helper(s, i-1)
                p2 = helper(i+1, e)
                if vals[i] == '+':
                    for x in p1:
                        for y in p2:
                            avail.append(x+y)
                elif vals[i] == '-':
                    for x in p1:
                        for y in p2:
                            avail.append(x-y)
                else:
                    for x in p1:
                        for y in p2:
                            avail.append(x*y)
            return avail
        return helper(0, len(vals)-1)


# @lc code=end
