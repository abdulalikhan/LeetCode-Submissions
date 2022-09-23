class Solution(object):
    def canVisitAllRooms(self, rooms):
        d = {}
        roomGraph = {}
        for i in range(len(rooms)):
            d[i] = 0
            roomGraph[i] = rooms[i]
        d[0] = 1
        stk = []
        stk.append(0)
        while len(stk)>0:
            thisNode = stk[-1]
            stk.pop()
            if d[thisNode] == 1:
                for neighbor in roomGraph[thisNode]:
                    if d[neighbor] == 0:
                        stk.append(neighbor)
                        d[neighbor] = 1
        for i in range(len(rooms)):
            if d[i] == 0:
                return False
        return True
        