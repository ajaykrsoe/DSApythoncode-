'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inorderHelper(self,root,ans):
        if(root):
            self.inorderHelper(root.left,ans)
            ans.append(root.data)
            self.inorderHelper(root.right,ans)

            
    def inOrder(self, root):
        # code here
        ans=[]
        self.inorderHelper(root,ans)
        return ans 
        
        
