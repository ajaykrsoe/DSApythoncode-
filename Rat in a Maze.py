class Solution:
    def pathFinder(self,maze,i,j,soFarPath,ans,n,visited) :
        if(i==n-1 and j==n-1):
            ans.append(soFarPath)
        visited[i][j]=1
        dirs=[(1,0,"D"),(0,-1,"L"),(0,1,"R"),(-1,0,"U")]
        for x,y,p in dirs:
            x+=i
            y+=j
            if(x>=0 and y>=0 and x<n and y<n and maze[x][y] and not visited[x][y]):
                self.pathFinder(maze,x,y,soFarPath+p,ans,n,visited)
        visited[i][j]=0
                
                
            
    
    
        
    def ratInMaze(self, maze):
        # code here
        ans=[]
        n=len(maze)
        visited=[[ 0 for e in range(n)] for x in range(n)]
        self.pathFinder(maze,0,0,"",ans,n,visited) 
        return ans 
        
    
