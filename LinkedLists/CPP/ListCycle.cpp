/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::detectCycle(ListNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    ListNode *slow = A;
    ListNode *fast = A;
    
    
    slow = slow->next;
    fast = fast->next->next;
    
    //znajdz miejsce spotkania, jest cykl, ale nie wiadomo jeszcze gdzie
    while (slow != fast){
        if (fast==NULL || fast->next==NULL || fast->next->next==NULL)return NULL;
        
        slow = slow->next;
        fast = fast->next;
        if (fast!=NULL)fast = fast->next;
    }
    
    fast = A;
    while(fast!=slow){
        fast=fast->next;//teraz oba z taką samą szybkością idą
        slow=slow->next;
    }
    return fast;
    
    
}
