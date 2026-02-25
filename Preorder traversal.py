'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrdeHelper(self,root,ans):
         if(root) :
             ans.append(root.data)
             self.preOrdeHelper(root.left,ans)
             self.preOrdeHelper(root.right,ans)

             
        
    def preOrder(self, root):
    # code here
        ans=[]
        self.preOrdeHelper(root,ans)
        return ans 
       
            
