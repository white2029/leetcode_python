#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (21.64%)
# Likes:    1714
# Dislikes: 245
# Total Accepted:    182.2K
# Total Submissions: 836.6K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
#
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#

# @lc code=start
from collections import defaultdict, deque
from functools import lru_cache
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        class Node:
            def __init__(self, w):
                self.w = w
                self.prev = set()

        def match(w1, w2):
            same = True
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    if same:
                        same = False
                    else:
                        return False
            return True

        words = wordList + [beginWord]
        conn = defaultdict(set)
        nodes = dict()
        for i, w1 in enumerate(words):
            nodes[w1] = Node(w1)
            for w2 in words[i+1::]:
                if match(w1, w2):
                    conn[w1].add(w2)
                    conn[w2].add(w1)
        if endWord not in nodes:
            return []
        #print(conn)
        to_visit = {beginWord}
        visited = set()
        success = False
        while to_visit:
            visited.update(to_visit)
            if endWord in visited:
                success = True
                break
            next_visit = set()
            for i in to_visit:
                for j in conn[i]:
                    if j not in visited:
                        nodes[j].prev.add(i)
                        next_visit.add(j)
            to_visit = next_visit
            #print(to_visit)

        if not success:
            return []

        @lru_cache(None)
        def recur(s):
            h = nodes[s]
            if not h.prev:
                return [[h.w]]
            tmp = []
            for i in h.prev:
                tmp += [x + [h.w] for x in recur(i)]
            return tmp
        return recur(endWord)



# @lc code=end
