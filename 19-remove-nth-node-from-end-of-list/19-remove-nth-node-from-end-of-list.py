class Solution(object):
    def removeNthFromEnd(self, head, n):
        c = 0
        noOfNodes = 0
        temp = head
        while temp != None:
            noOfNodes += 1
            temp = temp.next
        temp = head
        prev = None
        while temp != None:
            if prev != None and c == noOfNodes-n:
                prev.next = temp.next
            elif prev == None and c == noOfNodes-n:
                return head.next
            c += 1
            prev = temp
            temp = temp.next
        return head