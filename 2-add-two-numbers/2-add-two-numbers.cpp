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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sumList = new ListNode();
        ListNode* temp = sumList;
        int carry = 0, thisSum;
        while (l1 != NULL || l2 != NULL || carry != 0){
            thisSum = carry;
            thisSum += (l1 != NULL)? l1->val : 0;
            thisSum += (l2 != NULL)? l2->val : 0;
            carry = (thisSum)/10;
            ListNode* newNode = new ListNode(thisSum%10);
            sumList->next = newNode;
            sumList = sumList->next;
            l1 = (l1 != NULL)? l1->next : NULL;
            l2 = (l2 != NULL)? l2->next : NULL;
        }
        return temp->next;
    }
};