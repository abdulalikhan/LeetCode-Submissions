class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode* temp = head;
        ListNode* newList;
        ListNode* temp2;
        int i = 0;
        if (head == NULL)
            return head;
        while (temp != NULL){
            if (i == 0){
                newList = new ListNode(temp->val);
                temp2 = newList;
            }else if (i%2 == 0){
                ListNode* newNode = new ListNode(temp->val);
                temp2->next = newNode;
                temp2 = temp2->next;
            }
            i++;
            temp = temp->next;
        }
        i = 0;
        temp = head;
        while (temp != NULL){
            if (i%2 != 0){
                ListNode* newNode = new ListNode(temp->val);
                temp2->next = newNode;
                temp2 = temp2->next;
            }
            i++;
            temp = temp->next;
        }
        return newList;
    }
};