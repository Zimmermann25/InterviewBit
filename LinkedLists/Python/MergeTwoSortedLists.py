# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    '''def show(self, h):
        temp = h
        while temp != None:
            print(temp.val, end="")
            temp = temp.next'''
        
    def mergeTwoLists(self, A, B):
        
        # sortowanie rosnace, dopinam do A
        first = A
        second = B
        output = ListNode(-1)
        outTemp = output
        while True:
            if first is None:
                outTemp.next = second #jak dojdzie do konca pierwszej listy, to doklej pozostalosci drugiej
                break
            if second is None:
                outTemp.next = first#jak dojdzie do konca drugiej listy, to doklej pozostalosci pierwszej
                break
            if first.val <= second.val:
                outTemp.next = first
                first = first.next
            else:
                outTemp.next = second
                second = second.next
                
            outTemp = outTemp.next
            
        return output.next