class Solution(object):
    def printVertically(self, s):
        m = 0
        sList = s.split()
        for itm in sList:
            if len(itm) > m:
                m = len(itm)
        for i in range(len(sList)):
            if len(sList[i])<m:
                sList[i] = sList[i] + " "*(m-len(sList[i]))
        res = []
        for i in range(0, m):
            thisStr = ""
            for itm in sList:
                if i < len(itm):
                    thisStr += itm[i]
                else:
                    break
            res.append(thisStr.rstrip())
        return res