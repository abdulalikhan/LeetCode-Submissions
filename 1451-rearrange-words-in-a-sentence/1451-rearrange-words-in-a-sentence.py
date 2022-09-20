class Solution(object):
    def arrangeWords(self, text):
        text = text.lower().split()
        hq = []
        j = 0
        for i in range(len(text)):
                heapq.heappush(hq, (len(text[i]), j, text[i]))
                j += 1
        s = ""
        while len(hq)>0:
            if len(s)>0:
                s += ' ' + heapq.heappop(hq)[2]
            else:
                s += heapq.heappop(hq)[2].capitalize()
        return s