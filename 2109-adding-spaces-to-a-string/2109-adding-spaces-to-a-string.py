class Solution(object):
    def addSpaces(self, s, spaces):
        tempList = []
        prevIndex = 0
        for space in spaces:
            tempList.append(s[prevIndex:space])
            prevIndex = space
        tempList.append(s[prevIndex:])
        return " ".join(tempList)