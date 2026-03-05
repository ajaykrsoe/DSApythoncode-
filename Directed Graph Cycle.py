class Solution:
    def dfs(self,u,visited,adj,currentPath) :
        visited[u]=True
        currentPath[u]=True
        for v in adj[u] :
            if(visited[v] and currentPath[v]) :
                return True
            else :
                if self.dfs(v,visited,adj,currentPath) :
                    return True
        currentPath[u]=False
        return False 
            
    def isCyclic(self, V, edges):
        # code here
        visited=[False for e in range(V)]
        adj=[[] for e in range(V)]
        for u,v in edges :
            adj[u].append(v)
        curentPath=[False for e in range(V)]
        for u in range(V) :
            if(not visited[u] and self.dfs(u,visited,adj,curentPath) ):
                return True
        return False 
  
