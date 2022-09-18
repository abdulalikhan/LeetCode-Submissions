# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        dummyNode = ListNode()
        dummyNode.next = head
        sumDict = {0: dummyNode}
        runningSum = 0
        while temp:
            runningSum += temp.val
            if runningSum not in sumDict:
                sumDict[runningSum] = temp
            else:
                toRemove = sumDict[runningSum].next
                currSum = runningSum
                while toRemove and toRemove != temp:
                    currSum += toRemove.val
                    del sumDict[currSum]
                    toRemove = toRemove.next
                sumDict[runningSum].next = temp.next
            temp = temp.next
        return dummyNode.next