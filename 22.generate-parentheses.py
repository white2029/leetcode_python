#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (61.72%)
# Likes:    5096
# Dislikes: 264
# Total Accepted:    544.9K
# Total Submissions: 879.8K
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def sub(n):
            if n == 1:
                return {"()"}
            if n == 2:
                return {"()()", "(())"}
            rst = set()
            for i in range(1, n//2+1):
                v1 = sub(i)
                v2 = sub(n - i)
                if i == 1:
                    for j in v2:
                        rst.add("({})".format(j))
                for i in v1:
                    for j in v2:
                        rst.add("{}{}".format(i, j))
                        rst.add("{}{}".format(j, i))
            return rst
        return list(sorted(sub(n)))

# @lc code=end
