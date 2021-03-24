# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def show(self, A):
        while A:
            print(A)
            A = A.next
    
    def solve(self, A):
        # tylko zera i jednyki, wiec można zrobic w czasie O(N) (chyba xd)
        
        ones = 0
        zeros = 0
        temp =A
        while temp != None:
            if temp.val == 0:
                zeros +=1
            temp = temp.next
            
        
        temp = A
        counter = 0
        while temp != None:
            if counter < zeros:
                temp.val = 0
                counter +=1
            else:
                temp.val = 1
            temp = temp.next

        return A