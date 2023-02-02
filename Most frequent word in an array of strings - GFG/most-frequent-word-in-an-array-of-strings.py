import heapq
class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n):
        freq = {}
        hq = []
        for i in range(len(arr)):
            if arr[i] not in freq:
                freq[arr[i]] = [1, -i]
            else:
                freq[arr[i]][0] += 1
        for word in freq:
            heapq.heappush(hq, [-freq[word][0], freq[word][1], word])
        return heapq.heappop(hq)[2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[x for x in input().strip().split()]
        obj = Solution()
        print(obj.mostFrequentWord(arr,n))

# } Driver Code Ends