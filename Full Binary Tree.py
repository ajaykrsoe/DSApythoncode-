'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
        
# Return True if the given Binary Tree is a Full Binary Tree. Else return False
def isFullTree(root):
    #code here
    if(root):
        if(root.left and root.right ):
            lr=isFullTree(root.left)
            rr=isFullTree(root.right)
            if(lr and rr) :
                  return True
            return False 
        elif(not root.left and root.right )   or ( root.left and  not root.right) :
            return False
        else :
            return True 
            

