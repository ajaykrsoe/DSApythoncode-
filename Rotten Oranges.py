class Solution:
	def orangesRot(self, mat):
		# code here
		queue=[]
		m=len(mat)
		n=len(mat[0])
        for i in range(m):
            for j in range(n) :
                if(mat[i][j]==2) :
                    queue.append((i,j,0))
        totalTime=0
        dirs=[(0,-1),(0,1),(-1,0),(1,0)]
 
        while(queue) :
            i,j,t=queue.pop(0)
            for x,y in dirs :
                x+=i
                y+=j
                if(x>=0 and y>=0 and x<m and y<n  and mat[x][y]==1 ) :
                    mat[x][y]=2
                    totalTime=max(totalTime ,t+1)
                    queue.append((x,y,t+1))
        
        for i in range(m):
            for j in range(n) :
                if(mat[i][j]==1) :
                   return -1
        return totalTime       
   
        
        
        
