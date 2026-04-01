#User function Template for python3
from heapq import * 
class Node:
        def __init__(self,f,c) :
            self.f=f
            self.c=c
            self.left=None
            self.right=None

            
class Solution:
    def buildTree(self,S,F,N) :
        heap=[ ( F[i],i,Node(F[i],S[i]) )for  i in range(N)]
        heapify(heap)
        indx=N
        while len(heap)>1 :
            x=heappop(heap)
            y=heappop(heap)
            root=Node(x[0]+y[0],None)
            root.left=x[2]
            root.right=y[2]
            heappush(heap,(root.f,indx,root))
            indx+=1
        return heappop(heap)[2]
    def preorderTraversal(self,root,current_code,ans):
        if root is None:
            return
        if root.left is None and root.right is None:
            ans.append(current_code if current_code != "" else "0")
            return
        self.preorderTraversal(root.left,current_code+"0",ans)
        self.preorderTraversal(root.right,current_code+"1",ans)
   
            
            
    def huffmanCodes(self,S,f,N):
        # Code here
        root=self.buildTree(S,f,N)
        ans=[]
        self.preorderTraversal(root,"",ans)
        return ans 
  
            
