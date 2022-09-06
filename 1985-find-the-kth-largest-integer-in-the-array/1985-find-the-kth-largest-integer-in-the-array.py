class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        hq = []
        for num in nums:
            heapq.heappush(hq, -int(num))
        ans = -1
        while k>0:
            k -= 1
            ans = abs(heapq.heappop(hq))
        return str(ans)