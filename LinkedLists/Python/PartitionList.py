# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        #kolejne bezsensowne zadanie, które osobno można by było zrobić na wiele łatwiejszych sposobów
        
        if not A.next:
            return A
            
        else:
            #Add empty node at start
            empty_node = ListNode(-1)
            empty_node.next = A
            
            prev_node = empty_node
            p2 = A
            
            while(p2.val < B):
                p2 = p2.next
                prev_node = prev_node.next
            
            p1 = prev_node
            while(p2):
                if p2.val >=B:
                    p2 = p2.next
                    prev_node = prev_node.next
                else:
                    prev_node.next = p2.next
                    p2.next = p1.next
                    p1.next = p2
                    p1 = p2
                    p2 = prev_node.next
        return empty_node.next