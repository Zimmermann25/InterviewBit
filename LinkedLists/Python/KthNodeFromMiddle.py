# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # find middle first
        slow = A
        N = 0
        # znalezienie długości LL
        while slow is not None:
            N +=1
            slow = slow.next
            #fast = fast.next.next
        
        middle = (N//2) +1
        
        temp = A
        counter = 0
        isPossible = False
        #print("middle: ", middle, "diff: ", (middle - B))
        if (middle - B-1) >= 1:
            while counter < (middle - B-1):
                #print("c: ", counter, "diff: ",(middle - B), " val: ", temp.val )
                isPossible = True
                counter +=1
                temp = temp.next
        elif middle - B-1==0:
            return A.val
        
            
        
        if isPossible:return temp.val
        
        return -1