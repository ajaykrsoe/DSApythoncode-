'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        # code here
        if(root):
            lh=self.height(root.left)
            rh=self.height(root.right)
            return  1+max(lh,rh)

             
        return -1
    
