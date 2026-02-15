class Solution:
    def boundaryTraversal(self,mat):
        # code here 
        m=len(mat)
        n=len(mat[0])
        if(m==1):
            return mat[0]
        ans=[]
   
            
        ans=[]
        ans=ans+mat[0][0:n:]
        for r in range(1,m-1):
            ans.append(mat[r][-1])
        ans=ans+mat[-1][::-1]
        if(n!=1):
            for r in range(m-2,0,-1):
                ans.append(mat[r][0])
        return ans
        
    
