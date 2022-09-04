class Solution(object):
    def topKFrequent(self, nums, k):
        d = OrderedDict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        hq = []
        ans = []
        for num in d:
            heapq.heappush(hq, [-d[num], num])
        while k>0:
            ans.append(heapq.heappop(hq)[1])
            k -= 1
        return ans
        