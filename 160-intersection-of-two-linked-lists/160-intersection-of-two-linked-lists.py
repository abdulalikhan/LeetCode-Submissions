class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp = headA
        visitedSet = set()
        while temp != None:
            visitedSet.add(temp)
            temp = temp.next
        temp = headB
        while temp != None:
            if temp in visitedSet:
                return temp
            temp = temp.next
        return None