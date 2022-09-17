class Solution(object):
    def kthSmallest(self, matrix, k):
        tempList = []
        for i in matrix:
            tempList.extend(i)
        tempList.sort()
        return tempList[k-1]
            
        