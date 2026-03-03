class Solution:
    def dfsHelper(self,u,adj,visited,output):
        visited[u]=True
        output.append(u)
        for v in adj[u]:
             if(not visited[v]) :
                  self.dfsHelper(v,adj,visited,output)
    def dfs(self, adj):
        # code here
        n=len(adj)
        visited=[False for e in  adj]
        output=[]
        self.dfsHelper(0,adj,visited,output)
        return output
        
        
