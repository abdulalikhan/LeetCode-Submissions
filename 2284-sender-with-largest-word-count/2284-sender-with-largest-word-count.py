class CustomString:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word

    def __eq__(self, other):
        return self.word == other.word
    
    def __str__(self):
        return self.word
    
class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        d = {}
        maxheap = []
        for i in range(len(messages)):
            if senders[i] not in d:
                d[senders[i]] = len(messages[i].split())
            else:
                d[senders[i]] += len(messages[i].split())
        for itm in d:
            heapq.heappush(maxheap, [-d[itm], CustomString(itm)])
        return str(heapq.heappop(maxheap)[1])
        