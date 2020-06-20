#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (54.18%)
# Likes:    817
# Dislikes: 55
# Total Accepted:    57.2K
# Total Submissions: 105.6K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
#
#
#
# Example 1:
#
#
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
#
#
#
#
# Note:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
#
#
#
#
#
#

# @lc code=start
from collections import defaultdict
from functools import lru_cache
class Solution:
    def longestStrChain(self, words) -> int:
        def is_chain(w1, w2):
            skip = 0
            #print(w1, w2)
            for i,c in enumerate(w2):
                if i-skip >= len(w1) or  w1[i-skip] != c:
                    skip += 1
                    if skip > 1:
                        return False
            return True

        connect = defaultdict(set)
        lenw = defaultdict(set)
        for w in words:
            lenw[len(w)].add(w)
        lens = list(sorted(lenw.keys()))
        for i in lens:
            if i+1 in lenw:
                for w1 in lenw[i]:
                    for w2 in lenw[i+1]:
                        if is_chain(w1, w2):
                            connect[w2].add(w1)

        #print(connect)
        @lru_cache(maxsize=None)
        def get_depth(w):
            if not connect[w]:
                val = 1
            else:
                val = max([get_depth(x) for x in connect[w]]) +  1
            #print(w, val)
            return val

        return max([get_depth(w) for w in words])

#print(Solution().longestStrChain(["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"]))
# @lc code=end
