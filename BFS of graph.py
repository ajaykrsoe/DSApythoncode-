class Solution:
    def bfs(self, adj):
        # code here
        queue=[]
        n=len(adj)
        visited=[False for e in range(n)]
        visited[0]=True
        queue.append(0)
        output=[0]
        while(queue) :
            u=queue.pop(0)
            for v   in adj[u] :
                if(not visited[v]) :
                    output.append(v)
                    visited[v]=True
                    queue.append(v)
        return output 
            
