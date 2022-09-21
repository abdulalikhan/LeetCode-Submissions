class Solution(object):
    def middleNode(self, head):
        temp = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        temp = head
        mid = count//2
        i = 0
        while temp != None:
            if i == mid:
                return temp
            i += 1
            temp = temp.next