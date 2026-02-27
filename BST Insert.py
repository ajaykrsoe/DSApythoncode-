'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
#Method1
class Solution:
    def insert(self, root, key):
        # code here 
        if(not root) :
            return Node(key)
        if(key<root.data) :
            root.left=self.insert(root.left,key)
        else :
            root.right=self.insert(root.right,key)
        return  root
        


#method2
class Solution:
    def insertHelper(self,root,key) :
        if(key<root.data):
             if(root.left ):
                 self.insertHelper(root.left,key)
             else :
                 root.left=Node(key)
             
        else :
             if(root.right ):
                 self.insertHelper(root.right,key)
             else :
                 root.right=Node(key)
                         
        
    def insert(self, root, key):
        self.insertHelper(root,key)
        return  root
        
        
