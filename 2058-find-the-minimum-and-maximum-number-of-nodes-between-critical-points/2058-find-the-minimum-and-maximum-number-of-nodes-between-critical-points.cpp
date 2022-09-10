/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        ListNode* temp = head;
        ListNode* prev = NULL;
        int i = 1, lastI = 0, firstI = 0, minD = INT_MAX, maxD = -1;
        while (temp != NULL){
            if (temp->next != NULL && prev != NULL){
                if ((temp->val > prev->val && temp->val > temp->next->val) || (temp->val < prev->val && temp->val < temp->next->val)){
                    if (firstI == 0)
                        firstI = i;
                    else{
                        minD = min(minD, i-lastI);
                        maxD = max(maxD, i-firstI);
                    }
                    lastI = i;
                }
            }
            i++;
            prev = temp;
            temp = temp->next;
        }
        if (firstI == 0)
            return {-1, -1};
        minD = minD == INT_MAX?-1:minD;
        return {minD, maxD};
    }
};