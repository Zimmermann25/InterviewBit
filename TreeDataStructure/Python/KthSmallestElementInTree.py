# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    # to zadanie jest błędne dla powtarzających się liczb, nic nie jest napisane
    # co z nimi robić, czy pomijać, czy w lewo, czy w prawo
    # i jak kurwa wstawiać wartosci do test case, co oznaczają tam -1??
    def kthsmallest(self, A, B):
        #print("begin")
        '''counterArr = [0]
        def traverse(root):
            if counterArr[0]==B:return root.val

            if root.left is not None:
                traverse(root.left)
                
            if counterArr[0] == B:
                if root is not None:
                    return root.val
            counterArr[0] +=1
                    
            if root.right is not None:
                traverse(root.right)
                
        traverse(A)      '''
        
        l=[]
        def ino(root):
            if len(l)==B:
                return
            if root:
                ino(root.left)
                l.append(root.val)
                #print(root.val)
                ino(root.right)
        ino(A)
        return l[B-1]