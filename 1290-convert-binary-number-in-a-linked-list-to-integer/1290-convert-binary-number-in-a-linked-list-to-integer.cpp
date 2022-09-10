class Solution {
public:
    int getDecimalValue(ListNode* head) {
        ListNode* temp = head;
        int n = 0;
        long long int ans = 0;
        while (temp != NULL){
            n++;
            temp = temp->next;
        }
        temp = head;
        while (temp != NULL){
            ans += pow(2, --n)*temp->val;
            temp = temp->next;
        }
        return ans;
    }
};