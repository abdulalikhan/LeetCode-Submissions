class SeatManager(object):

    def __init__(self, n):
        self.hq = []
        for i in range(1, n+1):
            heapq.heappush(self.hq, i)
        

    def reserve(self):
        return heapq.heappop(self.hq)

    def unreserve(self, seatNumber):
        heapq.heappush(self.hq, seatNumber)