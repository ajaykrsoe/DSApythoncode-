class Solution:
    def printNearNodesHelper(self,root,low ,high,ans):
        if(root) :
            if(  root.data>=low and root.data<=high):
               
                self.printNearNodesHelper(root.left,low,high,ans)
                ans.append(root.data)
                self.printNearNodesHelper(root.right,low,high,ans)
                
            elif( root.data<low):
                self.printNearNodesHelper(root.right,low,high,ans)
            elif( root.data>high ):
              self.printNearNodesHelper(root.left,low,high,ans)
            
        
    def printNearNodes(self, root, low, high):
        #code here.
        ans=[]
        self.printNearNodesHelper(root,low,high,ans)
        return ans
        
        
