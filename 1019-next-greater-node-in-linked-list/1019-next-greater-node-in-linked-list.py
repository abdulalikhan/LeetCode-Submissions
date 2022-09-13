class Solution(object):
    def nextLargerNodes(self, head):
        temp = head
        tempList = []
        s = []
        ans = []
        while temp != None:
            tempList.append(temp.val)
            temp = temp.next
        while len(tempList) > 0:
            if len(s) == 0:
                ans.insert(0, '0')
                s.append(tempList[-1])
                tempList.pop()
            elif s[-1]>tempList[-1]:
                ans.insert(0, s[-1])
                s.append(tempList[-1])
                tempList.pop()
            else:
                s.pop()
        return ans