class Solution {
private:
    ListNode* listHead;
    int noOfNodes;
public:
    Solution(ListNode* head) {
        listHead = head;
        ListNode* temp = listHead;
        int count = 0;
        while (temp != NULL){
            count++;
            temp = temp->next;
        }
        noOfNodes = count;
    }
    
    int getRandom() {
        int index = rand()%noOfNodes;
        ListNode* temp = listHead;
        while (temp != NULL && index-- > 0)
            temp = temp->next;
        return temp->val;
    }
};