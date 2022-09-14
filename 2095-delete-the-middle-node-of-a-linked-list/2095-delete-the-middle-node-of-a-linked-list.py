class Solution(object):
    def deleteMiddle(self, head):
        temp = head
        n = 0
        while temp != None:
            n += 1
            temp = temp.next
        temp = head
        prev = None
        i = 0
        while temp != None:
            if i == (n//2) and prev != None:
                prev.next = temp.next
            elif i == (n//2) and prev == None:
                return head.next
            i += 1
            prev = temp
            temp = temp.next
        return head
        