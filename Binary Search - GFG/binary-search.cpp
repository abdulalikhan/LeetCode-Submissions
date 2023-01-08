//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:
    int binarysearchRec(int arr[], int n, int k, int l, int r)
    {
        if (l > r)
            return -1;
        int mid = (l+r)/2;
        if (arr[mid] == k)
            return mid;
        else if (arr[mid]>k)
            return binarysearchRec(arr, n, k, l, mid-1);
        else
            return binarysearchRec(arr, n, k, mid+1, r);
    }
    int binarysearch(int arr[], int n, int k) {
        return binarysearchRec(arr, n, k, 0, n-1);
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int N;
        cin >> N;
        int arr[N];
        for (int i = 0; i < N; i++) cin >> arr[i];
        int key;
        cin >> key;
        Solution ob;
        int found = ob.binarysearch(arr, N, key);
        cout << found << endl;
    }
}

// } Driver Code Ends