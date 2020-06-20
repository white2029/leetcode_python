#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (27.99%)
# Likes:    3347
# Dislikes: 133
# Total Accepted:    279.1K
# Total Submissions: 996.2K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#
#
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lls = len(s)
        def expand(pairs):
            rst = []
            change = False
            for i, j in pairs:
                while i>=1 and j<lls-1 and s[i-1]=='(' and s[j+1]==')':
                    i-=1
                    j+=1
                    change = True
                rst.append((i,j))
            return rst,change
        def merge(ps):
            change = False
            last_len = len(ps) + 1
            while len(ps) < last_len:
                last_len = len(ps)
                nps = []
                i=0
                while i<len(ps):
                    if i+1<len(ps):
                        if ps[i][1] == ps[i+1][0]-1:
                            nps.append((ps[i][0], ps[i+1][1]))
                            change = True
                            i+=2
                        else:
                            nps.append(ps[i])
                            i+=1
                    else:
                        nps.append(ps[i])
                        i+=1
                ps = nps
            return ps, change

        ini = []
        for i in range(0, lls-1):
            if s[i] =='(' and s[i+1]==')':
                ini.append((i, i+1))

        ini, __ = merge(ini)
        while True:
            ini_m, c_e = expand(ini)
            ini, c_m = merge(ini_m)
            if not c_e and not c_m:
                break
        return max([j-i+1 for i,j in ini]) if ini else 0

# @lc code=end
