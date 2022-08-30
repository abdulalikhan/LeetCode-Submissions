class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        resultList = []
        for word in words:
            differenceDict = {}
            inverseDict = {}
            possible = True
            for i in range(0, len(word)):
                if pattern[i] in inverseDict:
                    if inverseDict[pattern[i]] != word[i]:
                        possible = False
                        break
                if word[i] in differenceDict:
                    if pattern[i] != differenceDict.get(word[i]):
                        possible = False
                        break
                    elif pattern[i] in inverseDict:
                        if inverseDict[pattern[i]] != word[i]:
                            possible = False
                            break
                else:
                    differenceDict[word[i]] = pattern[i]
                    inverseDict[pattern[i]] = word[i]
            if possible:
                resultList.append(word)
        return resultList
        