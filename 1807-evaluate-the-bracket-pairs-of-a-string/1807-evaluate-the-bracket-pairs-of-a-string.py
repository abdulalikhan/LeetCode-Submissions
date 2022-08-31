class Solution(object):
    def evaluate(self, s, knowledge):
        newStr = ""
        startIndex = -1
        knowledgeDict = {k:v for k,v in knowledge}
        for i in range(0, len(s)):
            if s[i] == '(':
                startIndex = i
            elif s[i] == ')':
                key = s[startIndex+1:i]
                value = "?"
                if key in knowledgeDict:
                    value = knowledgeDict[key]
                newStr += value
                startIndex = -1
            elif startIndex == -1:
                newStr += s[i]
        return newStr