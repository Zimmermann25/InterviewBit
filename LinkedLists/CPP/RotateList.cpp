/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 //Mam dosyć tych list liniowych, nic tu nie działa, możliwości innych rozwiązań strasznie ograniczone
ListNode* Solution::rotateRight(ListNode* A, int B) {
    if(A==NULL || A->next==NULL)
        return A;
    ListNode *cur = A;
    int counter = 0;
    while(cur->next != NULL){
        cur = cur->next;
        counter += 1;
    }
    counter +=1;// bo cur->next
    cur->next = A;
    //cout<<"curN: "<<cur->val;
    //return cur;
    cur = A;
    B = B % counter;
    int startElem = counter - B; // ile elementów , indeksowanie od 0
    //cout<<"counter: "<<counter<<endl;
    
    for(int i=0; i<startElem-1; i++){
        cur = cur->next;
    }
    A = cur->next;
    cur->next = NULL;
    
    return A;
    
    
    
}