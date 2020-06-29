#
# @lc app=leetcode id=737 lang=python3
#
# [737] Sentence Similarity II
#
# https://leetcode.com/problems/sentence-similarity-ii/description/
#
# algorithms
# Medium (45.53%)
# Likes:    483
# Dislikes: 31
# Total Accepted:    40.2K
# Total Submissions: 88.2K
# Testcase Example:  '["great","acting","skills"]\n' +
#  '["fine","drama","talent"]\n' +
#  '[["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]'
#
# Given two sentences words1, words2 (each represented as an array of strings),
# and a list of similar word pairs pairs, determine if two sentences are
# similar.
#
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine",
# "drama", "talent"] are similar, if the similar word pairs are pairs =
# [["great", "good"], ["fine", "good"], ["acting","drama"],
# ["skills","talent"]].
#
# Note that the similarity relation is transitive. For example, if "great" and
# "good" are similar, and "fine" and "good" are similar, then "great" and
# "fine" are similar.
#
# Similarity is also symmetric. For example, "great" and "fine" being similar
# is the same as "fine" and "great" being similar.
#
# Also, a word is always similar with itself. For example, the sentences words1
# = ["great"], words2 = ["great"], pairs = [] are similar, even though there
# are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words.
# So a sentence like words1 = ["great"] can never be similar to words2 =
# ["doubleplus","good"].
#
# Note:
#
#
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
#
#
#
#
#

# @lc code=start
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        maps = dict()

        def sim(x, y):
            if x == y:
                return True
            if x not in maps:
                return False
            if y not in maps:
                return False
            return maps[x] is maps[y]

        def build(x):
            if x not in maps:
                xs = {x}
                maps[x] = xs

        def union(x, y):
            xs, ys = maps[x], maps[y]
            if xs is ys:
                return
            if len(xs) < len(ys):
                xs, ys = ys, xs
            xs.update(ys)
            for i in ys:
                maps[i] = xs

        if len(words1) != len(words2):
            return False

        for x, y in pairs:
            build(x)
            build(y)
            union(x, y)

        for i in range(len(words1)):
            if not sim(words1[i], words2[i]):
                return False
        return True

# @lc code=end
