
  struct ListNode {
      int val;
      struct ListNode *next;
 };
 


struct ListNode* reverseList(struct ListNode* head){
    
    if (head == NULL || head -> next == NULL){
        return head;
    }
    else{
    struct ListNode *prev = head;
    struct ListNode *current = head -> next;
    struct ListNode *next = current -> next;
    prev -> next = NULL;
    while (current != NULL){
        next = current -> next;
        current -> next = prev;
        prev = current;
        current = next;
    }
    
    return prev;
    }
    
}
