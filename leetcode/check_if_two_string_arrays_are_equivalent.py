"""
Runtime: 16 ms, faster than 91.04% of Python online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.5 MB, less than 53.61% of Python online submissions for Check If Two String Arrays are Equivalent.
"""
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        rtype = False

        wrd1_str = ''.join(word1)
        wrd2_str = ''.join(word2)

        if wrd1_str == wrd2_str:
            rtype = True

        return rtype


#word1 = ["ab", "cd"]
#word2 = ["a", "bcd"]
word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
#word1 = ['a']
#word2 = ['a']
solution = Solution.arrayStringsAreEqual(None, word1, word2)
print(solution)
