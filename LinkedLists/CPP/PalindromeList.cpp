/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
int Solution::lPalin(ListNode* A) {
    //najpierw zrobię stosem, choć doczytałem, że to jest zabronione xd
    //bez użycia stosu musiałbym stworzyć nową odwróconą listę i sprawdzić do połowy
    //długości listy
    //znalezc element mid, zapamiętać wskaznik, odrwócić pierwszą część i od pozycji
    //mid porównywać odwróconą listę z częścią pierwotnej od połowy
    //pierwsza część listy bez zmian, a druga połowa odwrócona
    ListNode *temp = A;
    stack<ListNode*> myStack;
    int counter = 0;
    while(temp !=NULL){
        myStack.push(temp);
        temp = temp->next;
        counter +=1;
    }
    
    counter = counter /2;
    
    temp = A;
    while( counter >=0 && temp != NULL && myStack.size()>0 ){
        if(myStack.top()->val != temp->val)return 0;
        counter -=1;
        temp = temp->next;
        myStack.pop();
    }
    
    return 1;
}