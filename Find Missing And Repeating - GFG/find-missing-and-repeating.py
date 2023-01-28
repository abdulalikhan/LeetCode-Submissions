#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        f = [0]*(n+1)
        x = y = -1
        for i in range(n):
            f[arr[i]] += 1
            if f[arr[i]] > 1:
                x = arr[i]
        for i in range(1, n+1):
            if f[i] == 0:
                y = i
        return x, y

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends