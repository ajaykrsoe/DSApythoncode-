'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def getNodes(self,root,nodes):
        if(root):
            nodes.append(root.data)
            self.getNodes(root.left,nodes)
            self.getNodes(root.right,nodes)
    def modifyNodes(self,root,nodes,nodeIndex) :
        if(root):
            lr=self.modifyNodes(root.left,nodes,nodeIndex)
            root.data=nodes[lr]
            rr=self.modifyNodes(root.right,nodes,lr+1)
            return rr
        else :
            return nodeIndex 
        
            
    def binaryTreeToBST(self, root):
        # code here
        nodes=[]
        self.getNodes(root,nodes)
        nodes.sort()
        self.modifyNodes(root,nodes,0)
        
