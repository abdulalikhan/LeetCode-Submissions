class Solution(object):
    def topKFrequent(self, words, k):
        d = OrderedDict()
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        hq = []
        ans = []
        for word in d:
            heapq.heappush(hq, [-d[word], word])
        while k>0:
            ans.append(heapq.heappop(hq)[1])
            k -= 1
        return ans
        
        