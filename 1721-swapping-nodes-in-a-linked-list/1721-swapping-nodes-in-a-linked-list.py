# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        currIndex = 1
        noOfNodes = 0
        temp = head
        temp2 = None
        temp3 = 0
        while temp != None:
            if noOfNodes == k-1:
                temp2 = temp
            noOfNodes += 1
            temp = temp.next
        temp = head
        while temp != None:
            if currIndex == noOfNodes-k+1:
                temp3 = temp.val
                temp.val = temp2.val
            currIndex += 1
            temp = temp.next
        temp = head
        currIndex = 1
        while temp != None:
            if currIndex == k:
                temp.val = temp3
            currIndex += 1
            temp = temp.next
        return head