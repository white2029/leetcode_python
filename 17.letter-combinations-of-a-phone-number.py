#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (46.15%)
# Likes:    3833
# Dislikes: 408
# Total Accepted:    603.4K
# Total Submissions: 1.3M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
#
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps={'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        def sub(i):
            if i == len(digits) - 1:
                return list(maps[digits[i]])
            return [x + v for x in maps[digits[i]] for v in sub(i+1)]
        if not digits:
            return []
        return sub(0)




# @lc code=end
