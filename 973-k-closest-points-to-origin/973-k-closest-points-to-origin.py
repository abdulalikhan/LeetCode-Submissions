class Solution(object):
    def getDistance(self, thisPoint):
        return sqrt(pow(thisPoint[0], 2)+pow(thisPoint[1], 2))
    
    def kClosest(self, points, k):
        hq = []
        result = []
        for point in points:
            heappush(hq, [self.getDistance(point),  point])
        c = 0
        while len(hq)>0:
            c += 1
            if c > k:
                break
            result.append(heapq.heappop(hq)[1])
        return result