#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (27.22%)
# Likes:    673
# Dislikes: 1572
# Total Accepted:    135.8K
# Total Submissions: 495.4K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
#
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
#
# Note:
#
#
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
#
#
# Example 1:
#
#
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
#
# Example 2:
#
#
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be",
# because the last line must be left-justified instead of fully-justified.
# ⁠            Note that the second line is also left-justified becase it
# contains only one word.
#
#
# Example 3:
#
#
# Input:
# words =
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#
#
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = []
        curr = 0
        for w in words:
            new_len = curr + len(w) + int(len(line)>0)
            if new_len <= maxWidth:
                line.append(w)
                curr = new_len
            else:
                lines.append(line)
                line = [w]
                curr = len(w)
        rst = []
        for l in lines:
            ttl = sum([len(w) for w in l])
            spa = len(l) - 1
            if spa == 0:
                rst.append(l[0] + ' '*(maxWidth-ttl))
            else:
                rem = (maxWidth - ttl) % spa
                ech = (maxWidth - ttl) // spa
                rst.append(''.join([v+' '*(ech*int(i!=len(l)-1)+int(i<rem)) for i,v in enumerate(l)]))
        last = ' '.join(line)
        last = last + ' ' * (maxWidth - len(last))
        rst.append(last)
        return rst

# @lc code=end
