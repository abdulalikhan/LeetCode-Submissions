class Solution {
public:
    int pairSum(ListNode* head) {
        int n = 0;
        ListNode* temp = head;
        while (temp != NULL){
            n++;
            temp = temp->next;
        }
        unordered_map<int, int> m;
        int i = 0, maxSum = 0;
        temp = head;
        while (temp != NULL){
            if (m.find(i) == m.end() && m.find(n-1-i) == m.end()){
                m.insert(make_pair(i, temp->val));
            }else if (m.find(i) != m.end()){
                m[i] += temp->val;
                if (m[i] > maxSum)
                    maxSum = m[i];
            }else if (m.find(n-1-i) != m.end()){
                m[n-1-i] += temp->val;
                if (m[n-1-i] > maxSum)
                    maxSum = m[n-1-i];
            }
            i++;
            temp = temp->next;
        }
        return maxSum;
    }
};