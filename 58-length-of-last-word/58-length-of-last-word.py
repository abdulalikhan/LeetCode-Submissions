class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])
        